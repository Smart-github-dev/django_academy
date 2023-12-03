import os
from django.contrib.auth.models import User
from accounting.models import Plans
import logging
import getpass


## Academy prepare script
def init_script():

    plans = [   {
                    'name': 'Basic',
                    'long_name': 'FuchiCorp Academy Basic plan',
                    'description': 'Live instructor lead classes and standups. Complete tickets, troubleshoot issues and assistance from instructors and senior FuchiCorp members.\r\n#### Access to the following:\r\n* Github Repos (limited)\r\n* All Student Videos\r\n* FuchiCorp tools (limited)\r\n*Oppurtinity to join our Internship on completion of course and tickets.*',
                    'schedule': '#### Class:\r\nMonday, Wednesday at 6 PM CST\r\n\r\n#### Standup: \r\nWednesday, Thursday, and Friday at 12 pm CST',
                    'price': '100',
                    'price_description': 'You pay $100 for one month',
                    'six_months_price': '372',
                    'six_months_description': 'Pay for 6 months $372 and save $120',
                    'year_price': '680',
                    'year_description': 'Pay for 12 months you pay $720 save $264',
                    'level': 1,
                    'option1': 'Access to main videos',
                    'option2': 'Access to all demos',
                    'option3': 'Access to services',
                    'markdown_content': "# Academy Subscription Terms v0.6.10 \r\n#fuchicorp/plans/all \r\n\r\n## Plans\r\n1. Basic free for one month\r\n2. Contributors are free after you finish basic \r\n3. Pro $55 monthly\r\n4. Premium $300 monthly\r\n\r\n\r\n\r\n## Basic\r\n1. First-week basic members will deploy cluster infrastructure\r\n2. Second week basic members will deploy common tools\r\n3. Third week team will deploy Python Java C# applications hello world\r\n4. Last week team will do review of the all tools and plans of academy \r\n5. Simple task on first sprint planing \r\n6. Require to join all meetings \r\n\r\n\r\n\r\n## Contributors\r\n1. Access to all contribution repos\r\n2. Access to work sessions\r\n3. Access to demos\r\n4. Access to review classes\r\n5. Access to meetings\r\n6. Require to join all meetings\r\n\r\n\r\n\r\n## Pro\r\n1. Access to repos limited repos\r\n2. Access to work sessions\r\n3. Access to demos\r\n4. Access to review classes\r\n5. Access to meetings\r\n6. Optional to do tickets\r\n7. Optional to join the meetings \r\n8. Optional to join standup\r\n\r\n\r\n\r\n## Premium \r\n1. Optional to do tickets \r\n2. Optional to join the meetings  \r\n3. Optional to join standup \r\n4. Employed students support\r\n5. Access to repos\r\n6. Access to demos \r\n7. Access to meetings\r\n8. You can request 2 hours per week individual support\r\n9. You can ask join the meetings and get help\r\n\r\n\r\n\r\n## FAQ\r\n1. When I am going to be moved to pro?\r\n\t1. Right after one month your Basic account will be expired and you will need to get PRO account\r\n\t2. You will be focus on the interviews and searching the job \r\n\t3. If you don't finish tickets or requests on estimated time\r\n\t4. if you are missing meetings or stand-ups\r\n\r\n\r\n2. Can my Basic account be extended?\r\n\t1. Yes you will need to show good activities then we will extend your basic account\r\n\t2. You will be working on ticket individually not with team to extend your basic account\r\n\t3. You will be joining all meetings and Joining stand-ups and mediatory meetings  \r\n\r\n\r\n3. Is FuchiCorp will do everything for my interview task?\r\n\t1. No FuchiCorp instructors will help you following\r\n\t\t1. Understand what needs to be done\r\n\t\t2. Create the documentation for the task so you properly demonstrate to the X company \r\n\t\t3. Help you to build and deploy the task if it's not conflicting with X companies requirement\r\n\t\t4. Since X company is trying to keep confidential everything you will not share any sensitive information with us\r\n\r\n\r\n4. Why I need premium account?\r\n\t1. To get support from FuchiCorp individually \r\n\t2. To get help from 5 pm call with everyone \r\n\t3. To have access to limited repos\r\n\t4. To have access to work sessions\r\n\t5. To have access to meetings\r\n\t6. Before you join an individual call you need to make sure everything from your end is ready docs and ticket descriptions etc...\r\n\r\n\r\n5. Will the premium account take care of my tickets from my company?\r\n\t1. No, everything within the company is confidential\r\n\t2. You should not share sensitive information with FuchiCorp\r\n\t3. We will help you with topics, not in details\r\n\t4. All accounts you are sharing with us should be your own and not companies\r\n\t5. You will need to document the ticket you are getting from X company and properly show us \r\n\r\n\r\n6. Where can I submit my tasks from my company?\r\n\t1. Everything will be on the academy so you can submit\r\n\t2. You will need to navigate to your profile and submit the request to help\r\n\t3. Within 48 hours we should be able to review and help"
                },
                {
                    'name': 'Contributor',
                    'long_name': 'FuchiCorp Contribution team',
                    'description': 'Live instructor lead classes and standups. Complete advance tickets, troubleshoot advance issues, present demos, create documentation and create/merge pull requests. Participate in Sprint Planning and more.\r\n\r\n#### Access to the following:\r\n* Github Repos (limited)\r\n* All Contributor demo videos\r\n* All Contributor work session videos\r\n* FuchiCorp tools\r\n\r\n#### Required Prerequisites\r\n* Complete Student Courses\r\n* Pass Interview with Instructor',
                    'schedule': '## Class \r\nTuesday, Thursday at 6 PM CST\r\n\r\n\r\n## Standup \r\nMonday, Tuesday,  Wednesday, Thursday, Friday at 12 pm CST',
                    'price': '55',
                    'price_description': 'You pay $100 for one month',
                    'six_months_price': '372',
                    'six_months_description': 'Pay for 6 months $372 and save $120',
                    'year_price': '0',
                    'year_description': '0',
                    'level': 2,
                    'option1': 'awdawdafswadadawdadawd',
                    'option2': 'Access to work sessions',
                    'option3': 'Access to work sessions',
                    'markdown_content': "# Academy Subscription Terms v0.6.10 \r\n#fuchicorp/plans/all \r\n\r\n## Plans\r\n1. Basic free for one month\r\n2. Contributors are free after you finish basic \r\n3. Pro $55 monthly\r\n4. Premium $300 monthly\r\n\r\n\r\n\r\n## Basic\r\n1. First-week basic members will deploy cluster infrastructure\r\n2. Second week basic members will deploy common tools\r\n3. Third week team will deploy Python Java C# applications hello world\r\n4. Last week team will do review of the all tools and plans of academy \r\n5. Simple task on first sprint planing \r\n6. Require to join all meetings \r\n\r\n\r\n\r\n## Contributors\r\n1. Access to all contribution repos\r\n2. Access to work sessions\r\n3. Access to demos\r\n4. Access to review classes\r\n5. Access to meetings\r\n6. Require to join all meetings\r\n\r\n\r\n\r\n## Pro\r\n1. Access to repos limited repos\r\n2. Access to work sessions\r\n3. Access to demos\r\n4. Access to review classes\r\n5. Access to meetings\r\n6. Optional to do tickets\r\n7. Optional to join the meetings \r\n8. Optional to join standup\r\n\r\n\r\n\r\n## Premium \r\n1. Optional to do tickets \r\n2. Optional to join the meetings  \r\n3. Optional to join standup \r\n4. Employed students support\r\n5. Access to repos\r\n6. Access to demos \r\n7. Access to meetings\r\n8. You can request 2 hours per week individual support\r\n9. You can ask join the meetings and get help\r\n\r\n\r\n\r\n## FAQ\r\n1. When I am going to be moved to pro?\r\n\t1. Right after one month your Basic account will be expired and you will need to get PRO account\r\n\t2. You will be focus on the interviews and searching the job \r\n\t3. If you don't finish tickets or requests on estimated time\r\n\t4. if you are missing meetings or stand-ups\r\n\r\n\r\n2. Can my Basic account be extended?\r\n\t1. Yes you will need to show good activities then we will extend your basic account\r\n\t2. You will be working on ticket individually not with team to extend your basic account\r\n\t3. You will be joining all meetings and Joining stand-ups and mediatory meetings  \r\n\r\n\r\n3. Is FuchiCorp will do everything for my interview task?\r\n\t1. No FuchiCorp instructors will help you following\r\n\t\t1. Understand what needs to be done\r\n\t\t2. Create the documentation for the task so you properly demonstrate to the X company \r\n\t\t3. Help you to build and deploy the task if it's not conflicting with X companies requirement\r\n\t\t4. Since X company is trying to keep confidential everything you will not share any sensitive information with us\r\n\r\n\r\n4. Why I need premium account?\r\n\t1. To get support from FuchiCorp individually \r\n\t2. To get help from 5 pm call with everyone \r\n\t3. To have access to limited repos\r\n\t4. To have access to work sessions\r\n\t5. To have access to meetings\r\n\t6. Before you join an individual call you need to make sure everything from your end is ready docs and ticket descriptions etc...\r\n\r\n\r\n5. Will the premium account take care of my tickets from my company?\r\n\t1. No, everything within the company is confidential\r\n\t2. You should not share sensitive information with FuchiCorp\r\n\t3. We will help you with topics, not in details\r\n\t4. All accounts you are sharing with us should be your own and not companies\r\n\t5. You will need to document the ticket you are getting from X company and properly show us \r\n\r\n\r\n6. Where can I submit my tasks from my company?\r\n\t1. Everything will be on the academy so you can submit\r\n\t2. You will need to navigate to your profile and submit the request to help\r\n\t3. Within 48 hours we should be able to review and help"
                },
                {
                    'name': 'Pro',
                    'long_name': 'FuchiCorp Professional plan',
                    'description': 'This option is for our professional members that have limited time to join live instructor lead classes and complete tickets. Professional Subscription has not attendance requirements.\r\n\r\n#### Access to the following:\r\n* Github Repos (limited)\r\n* Access to live classes and standups\r\n* All Contributor demo videos\r\n* All Contributor work session videos\r\n* FuchiCorp tools\r\n\r\n#### Required Prerequisits:\r\n* Complete Student Courses\r\n* Currently Employed in the IT field',
                    'schedule': '#### Class \r\nTuesday, Thursday at 6PM CST\r\n\r\n\r\n#### Standup \r\nMonday, Tuesday,  Wednesday, Thursday, Friday at 12 pm CST',
                    'price': '103',
                    'price_description': 'You pay $103 for one month',
                    'six_months_price': '498',
                    'six_months_description': 'Pay for 6 months $372 and save $120',
                    'year_price': '239.88',
                    'year_description': 'Pay for 12 months you pay $986 save $250',
                    'level': 3,
                    'option1': 'Access to FuchiCorp Videos',
                    'option2': 'Access to demos',
                    'option3': 'Access to work sessions',
                    'markdown_content': "# Academy Subscription Terms v0.6.10 \r\n#fuchicorp/plans/all \r\n\r\n## Plans\r\n1. Basic free for one month\r\n2. Contributors are free after you finish basic \r\n3. Pro $55 monthly\r\n4. Premium $300 monthly\r\n\r\n\r\n\r\n## Basic\r\n1. First-week basic members will deploy cluster infrastructure\r\n2. Second week basic members will deploy common tools\r\n3. Third week team will deploy Python Java C# applications hello world\r\n4. Last week team will do review of the all tools and plans of academy \r\n5. Simple task on first sprint planing \r\n6. Require to join all meetings \r\n\r\n\r\n\r\n## Contributors\r\n1. Access to all contribution repos\r\n2. Access to work sessions\r\n3. Access to demos\r\n4. Access to review classes\r\n5. Access to meetings\r\n6. Require to join all meetings\r\n\r\n\r\n\r\n## Pro\r\n1. Access to repos limited repos\r\n2. Access to work sessions\r\n3. Access to demos\r\n4. Access to review classes\r\n5. Access to meetings\r\n6. Optional to do tickets\r\n7. Optional to join the meetings \r\n8. Optional to join standup\r\n\r\n\r\n\r\n## Premium \r\n1. Optional to do tickets \r\n2. Optional to join the meetings  \r\n3. Optional to join standup \r\n4. Employed students support\r\n5. Access to repos\r\n6. Access to demos \r\n7. Access to meetings\r\n8. You can request 2 hours per week individual support\r\n9. You can ask join the meetings and get help\r\n\r\n\r\n\r\n## FAQ\r\n1. When I am going to be moved to pro?\r\n\t1. Right after one month your Basic account will be expired and you will need to get PRO account\r\n\t2. You will be focus on the interviews and searching the job \r\n\t3. If you don't finish tickets or requests on estimated time\r\n\t4. if you are missing meetings or stand-ups\r\n\r\n\r\n2. Can my Basic account be extended?\r\n\t1. Yes you will need to show good activities then we will extend your basic account\r\n\t2. You will be working on ticket individually not with team to extend your basic account\r\n\t3. You will be joining all meetings and Joining stand-ups and mediatory meetings  \r\n\r\n\r\n3. Is FuchiCorp will do everything for my interview task?\r\n\t1. No FuchiCorp instructors will help you following\r\n\t\t1. Understand what needs to be done\r\n\t\t2. Create the documentation for the task so you properly demonstrate to the X company \r\n\t\t3. Help you to build and deploy the task if it's not conflicting with X companies requirement\r\n\t\t4. Since X company is trying to keep confidential everything you will not share any sensitive information with us\r\n\r\n\r\n4. Why I need premium account?\r\n\t1. To get support from FuchiCorp individually \r\n\t2. To get help from 5 pm call with everyone \r\n\t3. To have access to limited repos\r\n\t4. To have access to work sessions\r\n\t5. To have access to meetings\r\n\t6. Before you join an individual call you need to make sure everything from your end is ready docs and ticket descriptions etc...\r\n\r\n\r\n5. Will the premium account take care of my tickets from my company?\r\n\t1. No, everything within the company is confidential\r\n\t2. You should not share sensitive information with FuchiCorp\r\n\t3. We will help you with topics, not in details\r\n\t4. All accounts you are sharing with us should be your own and not companies\r\n\t5. You will need to document the ticket you are getting from X company and properly show us \r\n\r\n\r\n6. Where can I submit my tasks from my company?\r\n\t1. Everything will be on the academy so you can submit\r\n\t2. You will need to navigate to your profile and submit the request to help\r\n\t3. Within 48 hours we should be able to review and help"
                },
                {
                    'name': 'Premium',
                    'long_name': 'FuchiCorp Academy Premium plan',
                    'description': 'This option is for our employeed members. Advance ticket assistance and individual mentoring. Please contact us for more details.\r\n\r\n#### Access to the following:\r\n* Github Repos (limited)\r\n* Access to live classes and standups\r\n* All demo videos\r\n* All work session videos\r\n* FuchiCorp tools\r\n* Individualized employed support\r\n\r\n#### Required Prerequisites:\r\n* Currently Employed in the IT field',
                    'schedule': '#### 101 Meetings \r\nYou will have access to schedule 101 meetings\r\n\r\n#### Standup \r\nAll meetings are optional to join',
                    'price': '600',
                    'price_description': 'You pay $600 for one month',
                    'six_months_price': '2100',
                    'six_months_description': 'Pay for 6 months $2100 and save $300',
                    'year_price': '6200',
                    'year_description': 'Pay for 12 months you pay $6200 save $1000',
                    'level': 4,
                    'option1': 'Access to all Videos',
                    'option2': 'Access to Github organization',
                    'option3': 'Access to meetings and sprint planning',
                    'markdown_content': "# Academy Subscription Terms v0.6.10 \r\n#fuchicorp/plans/all \r\n\r\n## Plans\r\n1. Basic free for one month\r\n2. Contributors are free after you finish basic \r\n3. Pro $55 monthly\r\n4. Premium $300 monthly\r\n\r\n\r\n\r\n## Basic\r\n1. First-week basic members will deploy cluster infrastructure\r\n2. Second week basic members will deploy common tools\r\n3. Third week team will deploy Python Java C# applications hello world\r\n4. Last week team will do review of the all tools and plans of academy \r\n5. Simple task on first sprint planing \r\n6. Require to join all meetings \r\n\r\n\r\n\r\n## Contributors\r\n1. Access to all contribution repos\r\n2. Access to work sessions\r\n3. Access to demos\r\n4. Access to review classes\r\n5. Access to meetings\r\n6. Require to join all meetings\r\n\r\n\r\n\r\n## Pro\r\n1. Access to repos limited repos\r\n2. Access to work sessions\r\n3. Access to demos\r\n4. Access to review classes\r\n5. Access to meetings\r\n6. Optional to do tickets\r\n7. Optional to join the meetings \r\n8. Optional to join standup\r\n\r\n\r\n\r\n## Premium \r\n1. Optional to do tickets \r\n2. Optional to join the meetings  \r\n3. Optional to join standup \r\n4. Employed students support\r\n5. Access to repos\r\n6. Access to demos \r\n7. Access to meetings\r\n8. You can request 2 hours per week individual support\r\n9. You can ask join the meetings and get help\r\n\r\n\r\n\r\n## FAQ\r\n1. When I am going to be moved to pro?\r\n\t1. Right after one month your Basic account will be expired and you will need to get PRO account\r\n\t2. You will be focus on the interviews and searching the job \r\n\t3. If you don't finish tickets or requests on estimated time\r\n\t4. if you are missing meetings or stand-ups\r\n\r\n\r\n2. Can my Basic account be extended?\r\n\t1. Yes you will need to show good activities then we will extend your basic account\r\n\t2. You will be working on ticket individually not with team to extend your basic account\r\n\t3. You will be joining all meetings and Joining stand-ups and mediatory meetings  \r\n\r\n\r\n3. Is FuchiCorp will do everything for my interview task?\r\n\t1. No FuchiCorp instructors will help you following\r\n\t\t1. Understand what needs to be done\r\n\t\t2. Create the documentation for the task so you properly demonstrate to the X company \r\n\t\t3. Help you to build and deploy the task if it's not conflicting with X companies requirement\r\n\t\t4. Since X company is trying to keep confidential everything you will not share any sensitive information with us\r\n\r\n\r\n4. Why I need premium account?\r\n\t1. To get support from FuchiCorp individually \r\n\t2. To get help from 5 pm call with everyone \r\n\t3. To have access to limited repos\r\n\t4. To have access to work sessions\r\n\t5. To have access to meetings\r\n\t6. Before you join an individual call you need to make sure everything from your end is ready docs and ticket descriptions etc...\r\n\r\n\r\n5. Will the premium account take care of my tickets from my company?\r\n\t1. No, everything within the company is confidential\r\n\t2. You should not share sensitive information with FuchiCorp\r\n\t3. We will help you with topics, not in details\r\n\t4. All accounts you are sharing with us should be your own and not companies\r\n\t5. You will need to document the ticket you are getting from X company and properly show us \r\n\r\n\r\n6. Where can I submit my tasks from my company?\r\n\t1. Everything will be on the academy so you can submit\r\n\t2. You will need to navigate to your profile and submit the request to help\r\n\t3. Within 48 hours we should be able to review and help"
                },
            ]

    for plan in plans:
        if db_table_exists('accounting_plans'):
            if not Plans.objects.filter(name=plan['name']).exists():
                plan_class = Plans(
                    name=plan['name'],
                    price=plan['price'],
                    long_name=plan['long_name'],
                    schedule=plan['schedule'],
                    level=plan['level'],
                    description=plan['description'],
                    markdown_content=plan['markdown_content'],
                    six_months_price=plan['six_months_price'],
                    six_months_description=plan['six_months_description'],
                    year_price=plan['year_price'],
                    year_description=plan['year_description'],
                    option1=plan['option1'],
                    option2=plan['option2'],
                    option3=plan['option3'],
                    )
                plan_class.save()

    ## Init script which is responsible to create admin user
    if os.environ.get('ADMIN_USER') and os.environ.get('ADMIN_PASSWORD'):

        ## If table is exist in system
        if db_table_exists('auth_user'):

            ## IF user not created in system init script will go ahead and try to create
            if not User.objects.filter(username=os.environ.get('ADMIN_USER')).exists():
                super_user = User.objects.create_user(os.environ.get('ADMIN_USER'), password=os.environ.get('ADMIN_PASSWORD'))
                super_user.is_superuser=True
                super_user.is_staff=True
                super_user.save()
                logging.warning(f"admin user <{os.environ.get('ADMIN_USER')}> has been created !!")

def db_table_exists(table_name, cursor=None):
    ## Function to check table exist or not
    try:

        ## Trying to connect to DB
        if not cursor:
            from django.db import connection
            cursor = connection.cursor()
        if not cursor:
            raise Exception
        return table_name in connection.introspection.table_names()
    except:
        raise Exception("unable to determine if the table '%s' exists" % table_name)
