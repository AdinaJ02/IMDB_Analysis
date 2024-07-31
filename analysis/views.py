from django.shortcuts import render
import pandas as pd

# Create your views here.
def index(request):
    df = pd.read_csv('https://raw.githubusercontent.com/LearnDataSci/articles/master/Python%20Pandas%20Tutorial%20A%20Complete%20Introduction%20for%20Beginners/IMDB-Movie-Data.csv')

    analysis = {
        'total_movies': df.shape[0],
        'average_rating': df['Rating'].mean(),
        'average_revenue': df['Revenue (Millions)'].mean(),
        'year_distribution': df['Year'].value_counts().to_dict(),
    }

    return render(request, 'index.html', {'analysis': analysis})