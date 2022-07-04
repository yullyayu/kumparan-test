# kumparan-test

Script automation test for website using pytest and selenium 

1. Download the repository from GitHub 
2. Preconditions:
a. Install Python and pip
b. Install Selenium
c. Install PyTest framework
d. Install chromedriver (Recommend use chrome versi <= versi 103)
4. Running tests
   pytest -v tests/news-tests/news-test.py 
5. Generated report
   pytest -v -s --html=report.html --self-contained-html tests/news-tests/news-test.py 

