from collective.grok import gs
from ploneun.policy import MessageFactory as _

@gs.importstep(
    name=u'ploneun.policy', 
    title=_('ploneun.policy import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('ploneun.policy.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
