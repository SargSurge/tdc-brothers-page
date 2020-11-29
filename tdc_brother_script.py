# TDC Website Brother HTML and CSS Generator
# Created by Sergio Perez 11/28/2020

def format_image_link(link):
    try:
        img_id = link.split('/')[5]
        return f'https://drive.google.com/uc?export=view&id={img_id}'
    except:
        raise Exception('Please input a Google Drive Link with correct permissions')

def first_last(name):
    try:
        name = name.split(' ')
        first, last = tuple(name)
        first, last = first.lower(), last.lower()
        return first, last
    except:
        raise Exception("Brother's name was not formatted correctly.\n Input should be as follows: John Doe\n If there is an exception, i.e. multiple last names, please fix in post.")

def generate_css(name,link):
    first, last = first_last(name)
    img_link = format_image_link(link)
    css = f'''#{first}-{last} {{
                background: center url('{img_link}');
                background-size: cover;
            }}'''
    return css

def generate_html(name,major,hometown,bio):
    first, last = first_last(name)
    html = f'''<div class="brother">
                <div class="brother-image" id="{first}-{last}"></div>
                <div class="brother-info">
                    <div class="event-title">{name}</div>
                    <div class="event-date">Major: {major}</div>
                    <div class="event-location">Hometown: {hometown}</div>
                    <div class="event-desc">{bio}</div>
                </div>
            </div>'''
    return html


if __name__ == '__main__':
    
    # User Input

    name = input('Input Brother Name: ')
    major = input('Input Brother Major: ')
    hometown = input('Input Brother Hometown: ')

    print("Enter/Paste the brother's bio. Ctrl-D or Ctrl-Z ( windows ) to save it.")
    contents = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        contents.append(line)
    bio = '\n'.join(contents)

    link = input('Input Google Drive Image Link: ')

    # Generate Output

    css = generate_css(name,link)
    html = generate_html(name,major,hometown,bio)

    # Print Output

    print('------------OUTPUT------------\n')
    print('CSS:\n')
    print(css)
    print('\n')
    print('HTML:\n')
    print(html)
    print('\n')
    print('------------END------------\n')
          






