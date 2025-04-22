class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if self.props:
            return ' '.join(map(lambda x: f"{x[0]}={x[1]}", self.props.items()))
        
    def __repr__(self):
        return f"{self.__class__.__name__}{self.tag, self.value, self.children, self.props}"