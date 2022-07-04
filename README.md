# kumparan-test

Script automation test for website using pytest and selenium 

- Download the repository from GitHub 
- Preconditions:
   1. Install Python and pip
   2. Install Selenium
   3. Install PyTest framework
   4. Install chromedriver (Recommend use chrome versi <= versi 103)
- Running tests
   pytest -v tests/news-tests/news-test.py 
- Generated report
   pytest -v -s --html=report.html --self-contained-html tests/news-tests/news-test.py 

