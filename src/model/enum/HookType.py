from enum import Enum


class HookType(Enum):

    H_FLEETMODE_SLIDESHOW_TOOLBAR_ACTIONS = 'h_fleetmode_slideshow_toolbar_actions'

    H_SLIDESHOW_TOOLBAR_ACTIONS_START = 'h_slideshow_toolbar_actions_start'
    H_SLIDESHOW_TOOLBAR_ACTIONS_END = 'h_slideshow_toolbar_actions_end'
    H_SLIDESHOW_CSS = 'h_slideshow_css'
    H_SLIDESHOW_JAVASCRIPT = 'h_slideshow_javascript'

    H_FLEET_TOOLBAR_ACTIONS_START = 'h_fleet_toolbar_actions_start'
    H_FLEET_TOOLBAR_ACTIONS_END = 'h_fleet_toolbar_actions_end'
    H_FLEET_CSS = 'h_fleet_css'
    H_FLEET_JAVASCRIPT = 'h_fleet_javascript'

    H_ROOT_CSS = 'h_root_css'
    H_ROOT_JAVASCRIPT = 'h_root_javascript'
    H_ROOT_NAV_ELEMENT_START = 'h_root_nav_element_start'
    H_ROOT_NAV_ELEMENT_END = 'h_root_nav_element_end'
    H_ROOT_FOOTER = 'h_root_footer'
