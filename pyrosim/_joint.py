

class Mixin(object):

    def _send_joint(self, *args):
        return self._send_entity('Joint', *args)

    def send_hinge_joint(self,
                         body1, body2,
                         anchor,
                         axis = (0, 0, 1),
                         joint_range = None,
                         # other parameters to be added
                         ):

        self._assert_body(body1, 'body1')
        self._assert_body(body2, 'body2')
        if joint_range is None:
            joint_range = (1, -1) # no stops

        try:
            len(joint_range)
        except:
            joint_range = (-joint_range, joint_range)

        assert(len(joint_range)) == 2

        return self._send_joint("HingeJoint",
                          body1, body2,
                          anchor,
                          axis,
                          joint_range)

    def send_slider_joint(self,
                          body1, body2,
                          axis = (0, 0, 1),
                          joint_range = 0.5):

        self._assert_body(body1, 'body1')
        self._assert_body(body2, 'body2')
        if joint_range is None:
            joint_range = (1, -1) # no stops
        try:
            len(joint_range)
        except:
            joint_range = (-joint_range, joint_range)
        else:
          assert(len(joint_range)) == 2, "joint_range must have 2 entries"

        assert(joint_range[1] >= joint_range[0]) , "Slider joint cannot have infinite range"

        return self._send_joint("SliderJoint",
                          body1, body2,
                          axis,
                          joint_range)
