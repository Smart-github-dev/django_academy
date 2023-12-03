from django_filters import CharFilter, FilterSet, ModelMultipleChoiceFilter, MultipleChoiceFilter, ModelChoiceFilter, DateFromToRangeFilter, DateFilter
from videos.models import VideoFolder
from accounting.models import Plans
from django import forms
from django.forms import DateInput
# from psycopg2.extras import DateRange

from django_filters.widgets import RangeWidget

class VideoFolderFilter(FilterSet):
    name                = CharFilter(field_name='name', lookup_expr='icontains', widget=forms.TextInput(attrs={'class': "form-control"}))
    subscription_plan   = ModelChoiceFilter( label='subscription_plan', queryset=Plans.objects.all())
    # start_date_range    = DateFromToRangeFilter(field_name='start_date_range', widget=forms.TextInput(attrs={'class': "form-control"}))
    # start_date_range    = DateFilter(field_name='created_date',lookup_expr=('lt'), widget=RangeWidget(attrs={'placeholder': 'YYYY/MM/DD'}) )
    start_date_range    = DateFilter(field_name='created_date',lookup_expr=('lt'))


    # end_date_range      = DateFromToRangeFilter(field_name='end_date_range', widget=forms.TextInput(attrs={'class': "form-control"}))
    # end_date_range = DateFilter(field_name='created_date',lookup_expr=('gt'), widget=RangeWidget(attrs={'placeholder': 'YYYY/MM/DD'}))
    end_date_range = DateFilter(field_name='created_date',lookup_expr=('gt'))


    def get_date_range(self, start_date_range, end_date_range):
        return Sample.objects.filter(sampledate__gte=start_date_range,
                                sampledate__lte=end_date_range)


    class Meta:
        model = VideoFolder
        fields = '__all__'
        widgets = {'start_date_range': DateInput(),}
        exclude = [ 'thumbnail_link', 'link', 'name']



# from videos.filters import VideoFolderFilter
# from videos.models import VideoFolder
# videos = VideoFolderFilter(queryset=VideoFolder.objects.all())
# videos = VideoFolderFilter(queryset=VideoFolder.objects.all(), {'start_date_range': '2021-06-09', 'end_date_range':'2022-06-09'})


# class MyFilter(FilterSet):
#     date = DateFromToRangeFilter()
#     class Meta:
#         model = VideoFolder
#         fields = ['created_date']

# ## This is not working
# videos = VideoFolderFilter({'start_date_range': '2021-06-09', 'end_date_range':'2022-06-09'})

# ## This is working
# videos = VideoFolderFilter({'start_date_range': '2022-02-03T04:18:18Z', 'end_date_range':'2022-06-03T04:18:18Z'})


# MyFilter({'created_date_before': '2022-02-03T04:18:18Z', 'created_date_after':'2022-06-03T04:18:18Z'})
