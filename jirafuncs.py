from jira.client import JIRA
import pandas as pd
import sqlite3
import xlsxwriter
import logging

# Settings
email = 'tsikib1@verifone.com'                              # Jira username 
password = 'My37187LGN!#'                           
api_token = "OTg2NjAxNzY0NTM3OqiK1W7fSLBzRFNFEGGJePQp4P93"  # Jira API token
server = 'https://jira.verifone.com/'                       # Jira server URL
jql = "creator = PhaneshR1"                                 # JQL 

# Get issues from Jira in JSON format
jira = JIRA(options={'server': server}, basic_auth= (email, password))
jira_issues = jira.search_issues(jql,maxResults=0)



# JSON to pandas DataFrame
issues = pd.DataFrame()
for issue in jira_issues:
    d = {
        'id':    issue.id,
        'key':   issue.key,
        'self':  issue.self,
        
        'assignee':        str(issue.fields.assignee),
        'creator' :        str(issue.fields.creator),
        'reporter':        str(issue.fields.reporter),
        'created' :        str(issue.fields.created),   
        'labels':          str(issue.fields.labels),
        'components':      str(issue.fields.components),
        'description':     str(issue.fields.description),
        'summary':         str(issue.fields.summary),
        'fixVersions':     str(issue.fields.fixVersions),
        'issuetype':       str(issue.fields.issuetype.name),
        'priority':        str(issue.fields.priority.name),
        'project':         str(issue.fields.project),
        'resolution':      str(issue.fields.resolution),
        'resolution_date': str(issue.fields.resolutiondate),
        'status':          str(issue.fields.status.name),
        'updated':         str(issue.fields.updated),
        'versions':        str(issue.fields.versions),
        
        'subtask':            str(issue.fields.issuetype.subtask),
        'status_description': str(issue.fields.status.description),
        'watchcount':         str(issue.fields.watches.watchCount),
    }
    issues = issues.append(d, ignore_index=True)    
    
    # DataFrame to SQLite
con = sqlite3.connect("jira-issues.db")
issues.to_sql("issues", con, if_exists="replace")
con.close() 

# Get data from SQLite
con = sqlite3.connect("jira-issues.db")
sql = "select issuetype, count(*) count from issues group by issuetype"
df = pd.read_sql_query(sql, con)
con.close() 

# Create Excel file
row = 1
col = 1
workbook = xlsxwriter.Workbook('jira-excel_test.xlsx')
header = workbook.add_format({'bold': True, 'align': 'center', 'bg_color': '#D8E4BC'})
center = workbook.add_format({'align': 'center'})
worksheet = workbook.add_worksheet('Summary')
worksheet.write(row, col, 'Issue Type', header)
worksheet.write(row, col + 1, 'Count', header)
row += 1
for index, dat in df.iterrows():
    worksheet.write(row + index, col, dat['issuetype'])
    worksheet.write(row + index, col + 1, int(dat['count']), center)
workbook.close()
