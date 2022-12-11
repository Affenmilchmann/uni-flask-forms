def html_element(name: str, content: str = '', close: bool = True, **kwargs):
    if 'kwargs' in kwargs: del kwargs['kwargs']
    if 'class_' in kwargs:
        kwargs['class'] = kwargs['class_']
        del kwargs['class_']
    parameters = ' '.join([f"{key}={val}" for key, val in kwargs.items()])
    if parameters: parameters = ' ' + parameters
    if close: return f"<{name}{parameters}>{content}</{name}>"
    else: return f"<{name}{parameters}{' ' + content if content else ''}>"
    
def html_list(items: list, **kwargs):
    items_string = ''
    for item in items:
        items_string += html_element('li', item)
    return html_element('ul', items_string, **kwargs)
    
def main():
    print(html_element("div", "hello"))
    print(html_list(['first', 'second', 123]))
    print(html_list(['i', 'am', html_element('b', 'THE'), 'list']))
    
if __name__ == '__main__':
    main()