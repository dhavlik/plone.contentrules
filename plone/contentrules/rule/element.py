from zope.interface import implements, Interface 

from interfaces import IRuleElement, IRuleCondition, IRuleAction

class RuleElement(object):
    """A rule element.
    
    Ordinarily, rule elements will be created via ZCML directives, which will
    register them as utilities.
    """
    
    implements(IRuleElement)

    title = u''
    description = u''
    for_ = Interface
    schema = None
    factory = None
    
    def __str__(self):
        return u"%s: %s"%(self.title, self.description)
    
class RuleCondition(RuleElement):
    """A rule condition.
    
    Rule conditions are just rule elements, but are registered under a more
    specific interface to enable the UI to differentate between different types
    of elements.
    """
    implements(IRuleCondition)
    
class RuleAction(RuleElement):
    """A rule action.
    
    Rule action are just rule elements, but are registered under a more
    specific interface to enable the UI to differentate between different types
    of elements.
    """
    implements(IRuleAction)