import datetime
import subprocess



# anime data list
data = open(
    r"C:\Users\Ghassen\Documents\my-github\anime-shorts\python\data.txt", "r")
html = open(
    r"C:\Users\Ghassen\Documents\my-github\anime-shorts\python\html.txt", "w")
html.write("""
       <table> 
            <thead> 
              <tr>
                <th>Name</th> 
                <th>Type</th> 
                <th>Duration</th> 
                <th>Links</th> 
              </tr> 
            </thead> 
        <tbody>
    """)
# Functions


def bring(string):
    return string[: string.find(",")]


def clear(string):
    return string[string.find(",") + 1:]
def find_img(string):
    if string.find("myanimelist") != -1:
        return "img/mal.png"
    elif string.find("anilist") != -1:
         return "img/anilist.png"
    elif string.find("youtu") != -1:
         return "img/youtube.png"
    else: return ""

# Backup file name
backup = (str(datetime.datetime.now()) +
          ".txt").replace(" ", "").replace(":", "-")
backup = r"C:\Users\Ghassen\Documents\my-github\anime-shorts\python\backup\backup" + backup
file_backup = open(backup, "w")
file_backup.write(data.read())
file_backup.close()

data.seek(0)
line = str(data.readline())
while line != "":
    line = line + ","
    links = []

    name = bring(line).strip()  # bring "name, ..."
    line = clear(line)  # delete "name, ..."
    type = bring(line).strip()
    line = clear(line)
    duration = bring(line).strip()
    line = clear(line)

    while line != "":
        links.append(bring(line))
        line = clear(line)

    # print(f"{name}\n{type}\n{duration}\n{links}")
    line = str(data.readline())

    html.write("""
        <tr>
            <td>""" + name.capitalize() + """</td>
                <td><span class=\"""" + type +"""\">"""+ type +"""</span></td>
                <td>"""+duration+"""<span class="small">MIN</span></td>
                <td>
    """)
    for i in range(len(links)):
        html.write("""
        <a href=\"""" + links[i]+"""\" target="_blank">
            <img src=\""""+ find_img(links[i]) +"""\" alt="">
        </a>
        """)
    html.write("""
            </td>
        </tr>""")

html.write("""
    </tbody>
    </table>""")


subprocess.Popen(r'explorer /select,"C:\Users\Ghassen\Documents\my-github\anime-shorts\python\html.txt"')
data.close()
