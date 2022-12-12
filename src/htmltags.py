def tag(name: str, content: str = '', close: bool = True, **kwargs):
    if 'class_' in kwargs:
        kwargs['class'] = kwargs['class_']
        del kwargs['class_']
    parameters = ' '.join([f"{key}={val}" for key, val in kwargs.items()])
    if parameters: parameters = ' ' + parameters
    if close: return f"<{name}{parameters}>{content}</{name}>"
    else: return f"<{name}{parameters}{' ' + content if content else ''}>"
    
def __l(l_type: str, items: list, **kwargs):
    items_string = ''
    for item in items:
        items_string += tag('li', item)
    return tag(l_type, items_string, **kwargs)
    
def ul(items: list, **kwargs):
    return __l('ul', items, **kwargs)
    
def ol(items: list, **kwargs):
    return __l('ol', items, **kwargs)
    
def main():
    print(tag("div", "hello"))
    print(ul(['first', 'second', 123]))
    print(ul(['i', 'am', tag('b', 'THE'), 'list'], class_="great"))
    
if __name__ == '__main__':
    main()