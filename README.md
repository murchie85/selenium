# INSTRUCTIONS   
  
# requirements 

`pip install selenium` 
  
# Chrome Driver 
https://sites.google.com/a/chromium.org/chromedriver/downloads  

# Starter Code 

  
- Make sure the download matches chrome version
- Make sure you enabled the 'untrusted developer'

  
```python
PATH = '/Users/adammcmurchie/2021/selenium/chromedriver'
driver = webdriver.Chrome(PATH)
```


# Elements  

Have: 

- ID
- Class
- Name
- Tag

Most common is ID name and class name for grepping.
Class is not unique so harder to search by

# FIND ELEMENT 

```
find_element_by_id
find_element_by_class_name
find_element_by_link_text
find_element_by_css_selector
find_element_by_tag_name
find_element by_xpath

```


# FIND ELEMENTS
```
find_elements_by_class_name
...
```

