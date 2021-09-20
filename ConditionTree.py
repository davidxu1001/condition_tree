import re

class Node(object):
    content = None

    def __init__(self, *args):
        super(Node, self).__init__(*args)
        self.content = None
      
    def set_content(self, branch:dict) -> dict:
      self.content = branch
      return self.content

    def normalize(self) -> None:
      """
      Break `node` down to a hieararchy of dictionary with each
      having either 0 or 2 children elements apart from the 
      relational operator.
      """
      return None
    
    def validate(self) -> bool:
      """
      Validate if this node is a legitimate combination of 
      items.
      """
      if not hasattr(self, 'content'):
        return False

      if not isinstance(self.content, dict):
        return False

      if 'children' in self.content.keys():
        if isinstance(self.content['children'], list):
          if 0 < len(self.content['children']):
            haschildren = True
          else:
            haschildren = False
        else:
          return False
      else:
        haschildren = False

      if 'operator' in self.content.keys():
        if isinstance(self.content['operator'], str):
          if 'AND' == self.content['operator'].upper() \
              or 'OR' == self.content['operator'].upper():
            hasoperator = True
          else:
            return False
        else:
          return False
      else:
        hasoperator = False

      if haschildren ^ hasoperator:
        return False

      if (not haschildren) and (not hasoperator):
        return True

      # True == haschildren and True == hasoperator 
      return all([i.validate() for i in self.content['children']])
    
    def validate_normalization(self) -> bool:
      """
      Validate if this node is a legitimate combination of
      items in normalized form. 
      """
      if not self.validate():
        return False

      # Check about normalization
      if self.content.
      return True
        
    def traverse(self) -> None:
      return None