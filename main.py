from bs4 import BeautifulSoup as bs
from selenium import webdriver

# output file
output_filename = "Job_list.csv"

# headers = "Company, Job_Position, Salary, Location, Link"
headers = "Company, Job_Position, Location,"
f = open(output_filename, 'w')
f.write(headers)
website = "www.jobstreet.com.my"
# start browser
driver = webdriver.Chrome('./chromedriver.exe')

# Get all HTML
# jobstreet
job_street_url = "https://www.jobstreet.com.my/en/job-search/intern-jobs/?createdAt=14d&job-type=internship&salary=0&salary-max=2147483647&specialization=508"
driver.get(job_street_url)
jS_html = driver.page_source  # html file for JobStreet
driver.close()  # close after getting html file

# parse html into BeautifulSoup
jS_bs = bs(jS_html, "html.parser")
js_container = jS_bs.findAll("div", {"class": "sx2jih0 zcydq81w"})

for j in js_container:
    job_pos = j.find("div", {"class": "sx2jih0 _2j8fZ_0 sIMFL_0 _1JtWu_0"})
    job_company = j.find("span")
    job_location = "Unknown"

    jAll = j.find_all("span", {'class': "sx2jih0 zcydq82b zcydq8r iwjz4h0"})
    job_location = "Unknown"
    job_salary = "Unknown"
    jAllS = j.find_all("span", {'class': "sx2jih0 zcydq82b _18qlyvc0 _18qlyvcv _18qlyvc3 _18qlyvc6"})

    if len(jAllS)>1:
        s = jAllS[-1].string
        if s != "SearchResults.job-card.text-salary-above" and s is not None:
            job_salary = s

    if jAll is not None:
        job_location = jAll[-1].string
    lst = [job_pos,job_company,job_location,job_salary]
    if None not in lst:
        job_pos = job_pos.string
        job_company = job_company.string

        f.write('"' + job_company + '"' + ',' + '"' + job_pos + '"' ',' + '"' + job_location + '"' + ',' + '"' + job_salary + '"' + "," + '"' + website + '"' + '\n')

# Get all HTML
# jora
driver = webdriver.Chrome('./chromedriver.exe')
jora_url = "https://my.jora.com/j?sp=facet&q=internship+computer+science&a=14d"
driver.get(jora_url)
jr_html = driver.page_source  # html file for Jora
driver.close()  # close after getting html file
website = "my.jora.com"
# parse html into BeautifulSoup
jr_bs = bs(jr_html, "html.parser")
jr_container = jr_bs.findAll("div", {"class": "job-container result organic-job"})
for j in jr_container:
    job_pos = j.find("h3", {"class": "job-title heading-large -no-margin-bottom"}).string
    job_company = j.find("span",{"class": "job-company"}).string
    job_location = j.find("span", {"class": "job-location"}).string
    jAll = j.findAll("div",{"class":"badge -default-badge"})
    job_salary = "Unknown"
    if len(jAll)>0:
        job_salary = jAll[-1].string

    f.write('"' + job_company + '"' + ',' + '"' + job_pos + '"' ',' + '"' + job_location + '"' +','+ '"' + job_salary+ '"'+","+'"' + website + '"'+'\n')

website = "www.ricebowl.my"
# start browser
driver = webdriver.Chrome('./chromedriver.exe')

# Get all HTML
# ricebowl
rb_url = "https://www.ricebowl.my/content/search/job?q=computer-science&jtype=1-Internship"
driver.get(rb_url)
rb_html = driver.page_source  # html file for ricebowl
driver.close()  # close after getting html file

# parse html into BeautifulSoup
rb_bs = bs(rb_html, "html.parser")
rb_container = rb_bs.findAll("div", {"class": "is-flex-ellipsis is-flex-grow-1 pl-3"})

for j in rb_container:
    job_pos = j.find("a").string.strip()
    job_company = j.find("div",{"class": "text-ellipsis"}).string.strip()
    job_location = j.p.text.strip().replace("\n        ",' ')
    job_salary = "Unknown"
    f.write('"' + job_company + '"' + ',' + '"' + job_pos + '"' ',' + '"' + job_location + '"' + ',' + '"' + job_salary + '"' + "," + '"' + website + '"' + '\n')
