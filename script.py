from requests import get, post
import json
from dateutil import parser
import datetime

# Module variables to connect to moodle api:
# Insert token and URL for your site here.
# Mind that the endpoint can start with "/moodle" depending on your installation.
KEY = "8cc87cf406775101c2df87b07b3a170d"
URL = "https://034f8a1dcb5c.eu.ngrok.io"
ENDPOINT = "/webservice/rest/server.php"


def rest_api_parameters(in_args, prefix='', out_dict=None):
    """Transform dictionary/array structure to a flat dictionary, with key names
    defining the structure.
    Example usage:
    >>> rest_api_parameters({'courses':[{'id':1,'name': 'course1'}]})
    {'courses[0][id]':1,
     'courses[0][name]':'course1'}
    """
    if out_dict == None:
        out_dict = {}
    if not type(in_args) in (list, dict):
        out_dict[prefix] = in_args
        return out_dict
    if prefix == '':
        prefix = prefix + '{0}'
    else:
        prefix = prefix + '[{0}]'
    if type(in_args) == list:
        for idx, item in enumerate(in_args):
            rest_api_parameters(item, prefix.format(idx), out_dict)
    elif type(in_args) == dict:
        for key, item in in_args.items():
            rest_api_parameters(item, prefix.format(key), out_dict)
    return out_dict


def call(fname, **kwargs):
    """Calls moodle API function with function name fname and keyword arguments.
    Example:
    >>> call_mdl_function('core_course_update_courses',
                           courses = [{'id': 1, 'fullname': 'My favorite course'}])
    """
    parameters = rest_api_parameters(kwargs)
    parameters.update(
        {"wstoken": KEY, 'moodlewsrestformat': 'json', "wsfunction": fname})
    # print(parameters)
    response = post(URL+ENDPOINT, data=parameters).json()
    if type(response) == dict and response.get('exception'):
        raise SystemError("Error calling Moodle API\n", response)
    return response

################################################
# Rest-Api classes
################################################


class LocalGetSections(object):
    """Get settings of sections. Requires courseid. Optional you can specify sections via number or id."""

    def __init__(self, cid, secnums=[], secids=[]):
        self.getsections = call('local_wsmanagesections_get_sections',
                                courseid=cid, sectionnumbers=secnums, sectionids=secids)


class LocalUpdateSections(object):
    """Updates sectionnames. Requires: courseid and an array with sectionnumbers and sectionnames"""

    def __init__(self, cid, sectionsdata):
        self.updatesections = call(
            'local_wsmanagesections_update_sections', courseid=cid, sections=sectionsdata)

################################################
# Example
################################################


courseid = "22"  # Exchange with valid id.
# Get all sections of the course.
sec = LocalGetSections(courseid)

# Output readable JSON, but print only summary
print(json.dumps(sec.getsections[1]['summary'], indent=4, sort_keys=True))

# Split the section name by dash and convert the date into the timestamp, it takes the current year, so think of a way for making sure it has the correct year!
month = parser.parse(list(sec.getsections)[1]['name'].split('-')[0])
# Show the resulting timestamp
print(month)
# Extract the week number from the start of the calendar year
print(month.strftime("%V"))

#  Assemble the payload
data = [{'type': 'num', 'section': 0, 'summary': '', 'summaryformat': 1, 'visible': 1 , 'highlight': 0, 'sectionformatoptions': [{'name': 'level', 'value': '1'}]}]

# Assemble the correct summary
summary = '<a href="https://mikhail-cct.github.io/ca3-test/wk1/">Week 1: Introduction</a><br><a href="https://mikhail-cct.github.io/ca3-tet/wk1/wk1.pdf"s>Week 1: Introduction.pdf</a><br><a href="https://drive.google.com/file/d/1vyPoSlUc5hcXajllDyaqMKvlJOiYxbNH/view?usp=sharing">Week 1: Introduction.mp4</a>'

# Assign the correct summary
data[0]['summary'] = summary

# Set the correct section number
data[0]['section'] = 1

# Write the data back to Moodle
sec_write = LocalUpdateSections(courseid, data)

sec = LocalGetSections(courseid)
print(json.dumps(sec.getsections[1]['summary'], indent=4, sort_keys=True))
####################################################################### Week 2
#  Assemble the payload
data = [{'type': 'num', 'section': 0, 'summary': '', 'summaryformat': 1, 'visible': 1 , 'highlight': 0, 'sectionformatoptions': [{'name': 'level', 'value': '1'}]}]

# Assemble the correct summary
summary = '<a href="https://mikhail-cct.github.io/ca3-test/wk2/">Week 2: Variables and Data Types</a><br><a href="https://mikhail-cct.github.io/ca3-test/wk2/wk2.pdf">Week 2: Variables and Data Types.pdf</a><br><a href="https://drive.google.com/file/d/1elgdm2482AMcARz_NUVTjg8KBPmoLTxj/view?usp=sharing">Week 2: Variables and Data Types.mp4</a>'

# Assign the correct summary
data[0]['summary'] = summary

# Set the correct section number
data[0]['section'] = 2

# Write the data back to Moodle
sec_write = LocalUpdateSections(courseid, data)

sec = LocalGetSections(courseid)
print(json.dumps(sec.getsections[1]['summary'], indent=4, sort_keys=True))

####################################################################### Week 3
#  Assemble the payload
data = [{'type': 'num', 'section': 0, 'summary': '', 'summaryformat': 1, 'visible': 1 , 'highlight': 0, 'sectionformatoptions': [{'name': 'level', 'value': '1'}]}]

# Assemble the correct summary
summary = '<a href="https://mikhail-cct.github.io/ca3-test/wk3/">Week 3: Operators and Conditionals</a><br><a href="https://mikhail-cct.github.io/ca3-test/wk3/wk3.pdf">Week 3: Operators and Conditionals.pdf</a><br><a href="https://drive.google.com/file/d/1_RgK_fcatlpGOSDn6yokgOEZAFxKmTlc/view?usp=sharing">Week 3: Operators and Conditionals.mp4</a>'

# Assign the correct summary
data[0]['summary'] = summary

# Set the correct section number
data[0]['section'] = 3

# Write the data back to Moodle
sec_write = LocalUpdateSections(courseid, data)

sec = LocalGetSections(courseid)
print(json.dumps(sec.getsections[1]['summary'], indent=4, sort_keys=True))

####################################################################### Week 4
#  Assemble the payload
data = [{'type': 'num', 'section': 0, 'summary': '', 'summaryformat': 1, 'visible': 1 , 'highlight': 0, 'sectionformatoptions': [{'name': 'level', 'value': '1'}]}]

# Assemble the correct summary
summary = '<a href="https://mikhail-cct.github.io/ca3-test/wk4/">Week 4: Loops & Functions</a><br><a href="https://mikhail-cct.github.io/ca3-test/wk4/wk4.pdf">Week 4: Loops & Functions.pdf</a><br><a href="https://drive.google.com/file/d/1AFfRgg3y_ebWYsmJmANSQYFgOeDnVnwJ/view?usp=sharing">Week 4: Loops & Functions.mp4</a>'

# Assign the correct summary
data[0]['summary'] = summary

# Set the correct section number
data[0]['section'] = 4

# Write the data back to Moodle
sec_write = LocalUpdateSections(courseid, data)

sec = LocalGetSections(courseid)
print(json.dumps(sec.getsections[1]['summary'], indent=4, sort_keys=True))

####################################################################### Recording

import requests

def download_file_from_google_drive(id, destination):
    URL1 = "https://drive.google.com/file/d/1wg0gkGZp19JJdTa8Zim3L1_jCH4vawa1"

    session = requests.Session()

    response = session.get(URL1, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL1, params = params, stream = True)

    save_response_content(response, destination)    

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None

def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)

if __name__ == "__main__":
    file_id = 'https://drive.google.com/file/d/1wg0gkGZp19JJdTa8Zim3L1_jCH4vawa1'
    destination = 'VIDEO.html'
    download_file_from_google_drive(file_id, destination)
  
    
  