from Products.CMFCore.utils import getToolByName

def upgrade_1000_to_1001(context):
    setup = getToolByName(context, 'portal_setup')
    cssregistry = getToolByName(context, 'portal_css')
    jsregistry = getToolByName(context, 'portal_javascripts')

#    setup.runImportStepFromProfile('profile-collective.js.fitvids:default',
#                                   'jsregistry', run_dependencies=False,
#                                   purge_old=False)
#   setup.runImportStepFromProfile('profile-collective.js.fitvids:default',
#                                   'cssregistry', run_dependencies=False,
#                                   purge_old=False)

#    To remove a css or js resources:
#    cssregistry.unregisterResource('++resource++collective.js.fitvids/XXX.css')
#    cssregistry.cookResources()
#    jsregistry.unregisterResource('++resource++collective.js.fitvids/XXX.js')
#    jsregistry.cookResources()
