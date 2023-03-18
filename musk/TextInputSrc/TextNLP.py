"""I want a webpage with a black background."""

"""The webpage should have a white background."""

"""object --- attribute ---- adjective"""

"""objectList = [webpage,elements,buttons,check boxes, drop down, footer, header, image, labels, link, Navbar , paragraph, text area, text box,]"""




class TextNLP:
    def __init__(self):
        self.output = []
        self.dictObject = {
            "ObjectList": ["Webpage","Button","Dropdown","Footer","Header","Label","Link","NavBar", "Paragraph", "TextArea", "TextBox","Image"],
            "Webpage": ["page", "webpage", "website", "site", "web"],
            "Button": ["button","buttons"],
            "Dropdown": ["drop","down","dropdown","dropdowns", "downs", "drops"],
            "Footer": ["footer","foot","end", "ending"],
            "Header": ["header", "head", "heading", "headers", "headings", "title", "titles", "caption" , "captions"],
            "Label": ["label", "labeling","labelling","tag", "tags","labels", "labellings", "labelings"],
            "Link": ["links","link","hyperlinks","hyperlink"],
            "NavBar": ["navigationBar", "bar", "navigation", "nav", "navbar", "menu" ,"toggle", "togglemenu", "togglebar", "navigationmenu", "navmenu"],
            "Paragraph": ["para", "paras", "paragraphs", "paragraph"],
            "TextArea": ["area", "areas", "textarea","textareas","inputarea"],
            "TextBox": ["box","input","textbox", "inputs", "boxes", "textboxes", "inputfields", "inputfield", "field", "fields"],
            "Image": ["img","image","images","photo","photos","photographs","photograph","picture","pictures","pics","pic"],
        }
        self.attr = {
            "Webpage": ["background", "font", "alignment"],
            "Button": ["background","font","border"],
            "Dropdown": ["background", "font","border"],
            "Footer": ["background", "font", "alignment","border"],
            "Header": ["font","alignment"],
            "Label": ["font","alignment","background"],
            "Link": ["font"],
            "NavBar": ["font", "background"],
            "Paragraph": ["font", "background", "border", "alignment"],
            "TextArea": ["background","font", "border"],
            "TextBox": ["background","font","border"],
            "Image": ["border"],
            "background": ["back", "ground", "theme", "backdrop", "background", "color", "colour", "colored", "coloured", "colors", "coloring","colouring", "colorings", "colourings"],
            "font": ["font", "fonts", "style", "styles"],
            "alignment": ["align", "alignment", "place", "placed", "aligned", "lined"],
            "border": ["border", "borders","outline","outlines","lining"],
        }
        self.advejtives = {
            "background": ["color"],
            "color": ["indianred","lightcoral","salmon","darksalmon","lightsalmon","crimson","red","firebrick","darkred","pink","lightpink","hotpink","deeppink","mediumvioletred","palevioletred","coral","tomato","orangered","darkorange","orange","gold","yellow","lightyellow","lemonchiffon","lightgoldenrodyellow","papayawhip","moccasin","peachpuff","palegoldenrod","khaki","darkkhaki","lavender","thistle","plum","violet","orchid","fuchsia","magenta","mediumorchid","mediumpurple","rebeccapurple","blueviolet","darkviolet","darkorchid","darkmagenta","purple","indigo","slateblue","darkslateblue","mediumslateblue","greenyellow","chartreuse","lawngreen","lime","limegreen","palegreen","lightgreen","mediumspringgreen","springgreen","mediumseagreen","seagreen","forestgreen","green","darkgreen","yellowgreen","olivedrab","olive","darkolivegreen","mediumaquamarine","darkseagreen","lightseagreen","darkcyan","teal","aqua","cyan","lightcyan","paleturquoise","aquamarine","turquoise","mediumturquoise","darkturquoise","cadetblue","steelblue","lightsteelblue","powderblue","lightblue","skyblue","lightskyblue","deepskyblue","dodgerblue","cornflowerblue","mediumslateblue","royalblue","blue","mediumblue","darkblue","navy","midnightblue","cornsilk","blanchedalmond","bisque","navajowhite","wheat","burlywood","tan","rosybrown","sandybrown","goldenrod","darkgoldenrod","peru","chocolate","saddlebrown","sienna","brown","maroon","white","snow","honeydew","mintcream","azure","aliceblue","ghostwhite","whitesmoke","seashell","beige","oldlace","floralwhite","ivory","antiquewhite","linen","lavenderblush","mistyrose","gainsboro","lightgray","silver","darkgray","gray","dimgray","lightslategray","slategray","darkslategray","black"],
            "font" : ["font-family","color"],
            "font-family": ["Ariel","Verdana","Tahoma", "Georgia", "Garamond", "Calibri", "Noto", "Futara", "Geneva", "Optima","Bookman", "Cambria", "Didot", "Georgia", "Palatino", "perpetua", "Rockwell" , "Baskerville", "Consolas", "Courier", "Monaco", "Florence", "Parkavenue", "Impact", "Brushstroke", "Luminari", "Chalkduster", "Blippo", "papyrus", "Copperplate", "Oldtown"],
            "alignment": ["right", "center", "left"],
            "right" : ["right", "rightly", "right-most","rightmost"],
            "center": ["centerally", "center", "central", "half", "centered" ,"middle","between"],
            "left": ["leftly", "left" ,"left-most","leftmost"],
            "border": ["color"],
        }
    """This is the main function"""      
    def process(self, string):
        string = string.lower()
        list = string.split(".")
        objectCurr = None
        attrCurr = None
        adjectCurr = None
        adjectCat = None
        listOfLists = []
        for statement in list:
            
            match = None
            if objectCurr == None:
                
                for x in self.dictObject["ObjectList"]:
                    words = statement.split(" ")
                    for k in self.dictObject[x]:
                        for word in words:
                            if word == k.lower():
                                match = x
                                objectCurr = match
                if objectCurr != None:
                    
                    match = None
                    for x in self.attr[objectCurr]:
                        for k in self.attr[x]:
                            for word in words: 
                                if word == k.lower():
                                    match = x
                                    attrCurr = match
                    if attrCurr != None:
                        
                        match = None
                        for x in self.advejtives[attrCurr]:
                            for k in self.advejtives[x]:
                                for word in words:
                                    if word == k.lower():
                                        match = k
                                        adjectCurr = match
                                        adjectCat = x
                        if objectCurr != None and attrCurr != None and adjectCurr != None:
                            listOfLists.append([objectCurr,attrCurr,adjectCurr,adjectCat])
                            objectCurr = None
                            attrCurr = None
                            adjectCurr = None
                            adjectCat = None
            else:
                    
                    words = statement.split(" ")
                    if attrCurr == None:
                        match = None
                        for x in self.attr[objectCurr]:
                            for k in self.attr[x]:
                                for word in words: 
                                    if word == k.lower():
                                        match = x
                                        attrCurr = x
                        if attrCurr != None:
                            match = None
                            for x in self.advejtives[attrCurr]:
                                for k in self.advejtives[x]:
                                    for word in words:
                                        if word == k.lower():
                                            match = k
                                            adjectCurr = match
                                            adjectCat = x
                            if objectCurr != None and attrCurr != None and adjectCurr != None:
                                listOfLists.append([objectCurr,attrCurr,adjectCurr,adjectCat])
                                objectCurr = None
                                attrCurr = None
                                adjectCurr = None
                                adjectCat = None
                    else:
                        words = statement.split(" ")
                        if adjectCurr == None:
                            match = None
                            for x in self.advejtives[attrCurr]:
                                for k in self.advejtives[x]:
                                    for word in words:
                                        if word == k.lower():
                                            match = k
                                            adjectCurr = match
                                            adjectCat = x
                            if objectCurr != None and attrCurr != None and adjectCurr != None:
                                listOfLists.append([objectCurr,attrCurr,adjectCurr,adjectCat])
                                objectCurr = None
                                attrCurr = None
                                adjectCurr = None
                                adjectCat = None

        return listOfLists

