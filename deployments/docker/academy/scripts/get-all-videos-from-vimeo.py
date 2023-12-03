from videos.models import VideoFolder
from common import Lucy
from datetime import timedelta
from accounting.models import Plans


def run():
    ## Getting vimeo client
    vimeo_cleint = Lucy()

    ## Getting all folders from vimeo
    vimeo_parent_folders = vimeo_cleint.get_parent_folders()
    ## list to store all folders which is already in database
    db_folders = []

    ## Looping all folders in vimeo

    while len(vimeo_parent_folders) != 0:
        for vimeo_folder in vimeo_parent_folders:
            if 'folder' in vimeo_folder.keys():
                if not VideoFolder.objects.filter(name=vimeo_folder['folder']['name']).exists():

                    ## Creating folder in database and saving to database
                    db_folder = VideoFolder(
                        type='folder',
                        name=vimeo_folder['folder']['name'],
                        vimeo_name=vimeo_folder['folder']['name'],
                        total_items=vimeo_folder['folder']['metadata']['connections']['items']['total'],
                        resource_key=vimeo_folder['folder']['resource_key'],
                        description='thisi-folder-description',
                        created_date=vimeo_cleint.get_date_time_format(vimeo_folder['folder']['created_time']),
                        updated_date=vimeo_cleint.get_date_time_format(vimeo_folder['folder']['modified_time']),
                        is_parent=True,
                        has_child=True
                        )

                    db_folder.save()

                    ## Storing db instances to loop it later
                    db_folders.append(db_folder)
                else:
                    ## Making sure the script will keep adding thanks to this line
                    db_folders.append(VideoFolder.objects.filter(name=vimeo_folder['folder']['name']).first())

            if vimeo_folder['folder']['metadata']['connections']['items']['total'] >= 0:
                parent = VideoFolder.objects.filter(name=vimeo_folder['folder']['name']).first()

                child_items = vimeo_cleint.get_child_items(vimeo_folder['folder']['uri'])

                for child_folder in child_items['folders']:
                    if not VideoFolder.objects.filter(name=child_folder['folder']['name']).exists():

                        db_folder = VideoFolder(
                            type='folder',
                            name=child_folder['folder']['name'],
                            vimeo_name=child_folder['folder']['name'],
                            resource_key=child_folder['folder']['resource_key'],
                            total_items=child_folder['folder']['metadata']['connections']['items']['total'],
                            created_date=vimeo_cleint.get_date_time_format(child_folder['folder']['created_time']),
                            updated_date=vimeo_cleint.get_date_time_format(child_folder['folder']['modified_time']),
                            is_parent=False,
                            has_child=True,
                            parent_resource_key=parent.resource_key,
                            parent=parent
                            )

                        db_folder.save()
                        ## Storing db instances to loop it later
                        db_folders.append(db_folder)

                    else:
                        ## Making sure the script will keep adding thanks to this line
                        db_folders.append(VideoFolder.objects.filter(name=child_folder['folder']['name']).first())

                    if child_folder['folder']['metadata']['connections']['items']['total'] >= 0:
                        vimeo_parent_folders.append(child_folder)

                for video in child_items['videos']:

                    if not VideoFolder.objects.filter(resource_key=video['video']['resource_key']).exists():

                        ## Create instance of the video and store in database with proper folder
                        # video_topic = VideoTopic.objects.get(name=topic_name, folder=folder)
                        subscription_plan = [f"#{x.name}" for x in Plans.objects.all()]

                        if video['video']["description"]:
                            video_plan = [ele.lower() for ele in subscription_plan if(ele.lower() in video['video']["description"] and ele is not None)]
                            if video_plan:
                                video_plan = video_plan[0].replace('#', '')
                            else:
                                video_plan = 'Premium'
                        if 'video_plan' not in locals():
                            video_plan = 'Premium'

                        subscription_plan = Plans.objects.get(name=video_plan)

                        ## Storing video inside database
                        video_id, video_share = video['video']['link'].split('/')[-2:]
                        video_link = f"https://player.vimeo.com/video/{video_id}?h={video_share}"
                        if 'vimeo.com' in video_id:
                            video_link = f"https://player.vimeo.com/video/{video_share}"


                        video = VideoFolder(
                            type='video',
                            resource_key=video['video']['resource_key'],
                            name=video['video']['name'],
                            description=video['video']["description"],
                            duration=timedelta(seconds=video['video']["duration"]),
                            link=f"{video_link}",
                            thumbnail_link=video['video']['pictures']['sizes'][-1]['link'],
                            has_child=False,
                            created_date=vimeo_cleint.get_date_time_format(video['video']['created_time']),
                            updated_date=vimeo_cleint.get_date_time_format(video['video']['modified_time']),
                            total_views=video['video']["stats"]['plays'],
                            subscription_plan=subscription_plan,
                            plan_level=subscription_plan.level,
                            parent=parent
                        )
                        video.save()

            vimeo_parent_folders.remove(vimeo_folder)
