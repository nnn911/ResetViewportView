from ovito.gui import UtilityInterface
from ovito.traits import action_handler
from traits.api import Button
from ovito import scene
from ovito.vis import Viewport


class ResetViewportView(UtilityInterface):

    btn = Button(ovito_label="Reset viewport view")

    @action_handler("btn")
    def run(self):
        scene.viewports.active_vp.type = Viewport.Type.Perspective
        scene.viewports.active_vp.fov = 0.610865238198
        scene.viewports.active_vp.camera_dir = (
            -0.49923017660270624,
            0.665640235470275,
            -0.5547001962252291,
        )
        scene.viewports.active_vp.camera_pos = (
            14.000942985459858,
            -18.667923980613143,
            15.55660331717762,
        )
        scene.viewports.active_vp.zoom_all()
