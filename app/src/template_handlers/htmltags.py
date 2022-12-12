from pprint import pprint

def tag(name: str, content: str = '', close: bool = True, **kwargs):
    parsed_kwargs = {}
    for k in kwargs.keys():
        parsed_kwargs[k.replace('_', '')] = kwargs[k]
    parameters = ' '.join([f'{key}="{val}"' for key, val in parsed_kwargs.items()])
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

def input_(**kwargs):
    return tag('input', close=False, **kwargs)

def label(content, **kwargs):
    return tag('label', content, **kwargs)

def form(content, **kwargs):
    if isinstance(content, str):
        return tag('form', content, **kwargs)
    elif isinstance(content, list):
        return tag('form', '<br>'.join(content), **kwargs)

#############################
    
def main():
    pprint(tag("div", "hello"))
    pprint(ul(['first', 'second', 123]))
    pprint(ul(['i', 'am', tag('b', 'THE'), 'list'], class_="great"))
    pprint(input_(type="text", size=40))
    pprint(label("I am a label", id="lol", for_="me"))
    
if __name__ == '__main__':
    main()