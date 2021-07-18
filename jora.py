from bs4 import BeautifulSoup as bs
from selenium import webdriver

# output file
output_filename = "Job_list.csv"

# headers = "Company, Job_Position, Salary, Location, Link"
headers = "Company, Job_Position, Location, Salary\n"
f = open(output_filename, 'w')
f.write(headers)

# start browser
driver = webdriver.Chrome('./chromedriver.exe')

# Get all HTML
# jobstreet
jora_url = "https://my.jora.com/j?sp=facet&q=internship+computer+science&a=14d"
driver.get(jora_url)
jr_html = driver.page_source  # html file for JobStreet
driver.close()  # close after getting html file

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

    f.write('"' + job_company + '"' + ',' + '"' + job_pos + '"' ',' + '"' + job_location + '"' +','+ '"' + job_salary+ '"'+'\n')