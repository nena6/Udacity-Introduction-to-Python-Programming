#Write the html_list function. The function takes one argument, a list of strings, and returns a single string which is an HTML list. For example, if the function should produce the following string when provided the list ['first string', 'second string'].
#define the  html_list function

def html_list(htmllist):
    my_list=["<ul>"]
    html_string=""
    for html in htmllist:
        my_list.append("<li>"+html+"</li>")
    my_list.append("</ul>")

   # for element in my_list:
    #    html_string+=element
    #join returns string
    return ("\n".join(my_list))

list1=['first string', 'second string']
print(html_list(list1))

#Udacity solution

def html_list(list_items):
    HTML_string = "<ul>\n"
    for item in list_items:
        HTML_string += "<li>{}</li>\n".format(item)
    HTML_string += "</ul>"
    return HTML_string
