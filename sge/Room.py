# The SGE Specification
# Written in 2012, 2013, 2014, 2015 by Julian Marchant <onpon4@riseup.net> 
# 
# To the extent possible under law, the author(s) have dedicated all
# copyright and related and neighboring rights to this software to the
# public domain worldwide. This software is distributed without any
# warranty. 
# 
# You should have received a copy of the CC0 Public Domain Dedication
# along with this software. If not, see
# <http://creativecommons.org/publicdomain/zero/1.0/>.

# INSTRUCTIONS FOR DEVELOPING AN IMPLEMENTATION: Replace  the notice
# above as well as the notices contained in other source files with your
# own copyright notice.  Recommended free  licenses are  the GNU General
# Public License, GNU Lesser General Public License, Expat License, or
# Apache License.

import sge


class Room(object):

    """
    This class stores the settings and objects found in a room.  Rooms
    are used to create separate parts of the game, such as levels and
    menu screens.

    .. attribute:: width

       The width of the room in pixels.  If set to :const:`None`,
       :attr:`sge.game.width` is used.

    .. attribute:: height

       The height of the room in pixels.  If set to :const:`None`,
       :attr:`sge.game.height` is used.

    .. attribute:: views

       A list containing all :class:`sge.View` objects in the room.

    .. attribute:: background

       The :class:`sge.Background` object used.

    .. attribute:: background_x

       The horizontal position of the background in the room.

    .. attribute:: background_y

       The vertical position of the background in the room.

    .. attribute:: alarms

       A dictionary containing the alarms of the room.  Each value
       decreases by 1 each frame (adjusted for delta timing if it is
       enabled).  When a value is at or below 0,
       :meth:`sge.Room.event_alarm` is executed with ``alarm_id`` set to
       the respective key, and the item is deleted from this dictionary.

    .. attribute:: objects

       A list containing all :class:`sge.Object` objects in the
       room.  (Read-only)

    .. attribute:: rd

       Reserved dictionary for internal use by the SGE.  (Read-only)
    """

    def __init__(self, objects=(), width=None, height=None, views=None,
                 background=None, background_x=0, background_y=0):
        """
        Arguments:

        - ``views`` -- A list containing all :class:`sge.View` objects
          in the room.  If set to :const:`None`, a new view will be
          created with ``x=0``, ``y=0``, and all other arguments
          unspecified, which will become the first view of the room.
        - ``background`` -- The :class:`sge.Background` object used.  If
          set to :const:`None`, a new background will be created with no
          layers and the color set to black.

        All other arguments set the respective initial attributes of the
        room.  See the documentation for :class:`sge.Room` for more
        information.
        """
        # TODO

    def add(self, obj):
        """
        Add an object to the room.

        Arguments:

        - ``obj`` -- The :class:`sge.Object` object to add.

        """
        # TODO

    def remove(self, obj):
        """
        Remove an object from the room.

        Arguments:

        - ``obj`` -- The :class:`sge.Object` object to remove.
        """
        # TODO

    def start(self, transition=None, transition_time=1500,
              transition_arg=None):
        """
        Start the room.

        Arguments:

        - ``transition`` -- The type of transition to use.  Should be
          one of the following:

          - :const:`None` (no transition)
          - ``"fade"`` (fade to black)
          - ``"dissolve"``
          - ``"pixelate"``
          - ``"wipe_left"`` (wipe right to left)
          - ``"wipe_right"`` (wipe left to right)
          - ``"wipe_up"`` (wipe bottom to top)
          - ``"wipe_down"`` (wipe top to bottom)
          - ``"wipe_upleft"`` (wipe bottom-right to top-left)
          - ``"wipe_upright"`` (wipe bottom-left to top-right)
          - ``"wipe_downleft"`` (wipe top-right to bottom-left)
          - ``"wipe_downright"`` (wipe top-left to bottom-right)
          - ``"wipe_matrix"``
          - ``"iris_in"``
          - ``"iris_out"``

          If an unsupported value is given, default to :const:`None`.

        - ``transition_time`` -- The time the transition should take in
          milliseconds.  Has no effect if ``transition`` is
          :const:`None`.

        - ``transition_arg`` -- An arbitrary argument that can be used
          by the following transitions:

          - ``"fade"`` -- A :class:`sge.Color` object indicating the
            color to fade to.  Default is black.
          - ``"wipe_matrix"`` -- The size of each square in the matrix
            transition as a tuple in the form ``(w, h)``, where ``w`` is
            the width and ``h`` is the height.  Default is ``(4, 4)``.
          - ``"iris_in"`` and ``"iris_out"`` -- The position of the
            center of the iris as a tuple in the form ``(x, y)``, where
            ``x`` is the horizontal location relative to the window and
            ``y`` is the vertical location relative to the window.
            Default is the center of the window.
        """
        # TODO

    def project_dot(self, x, y, z, color):
        """
        Project a single-pixel dot onto the room.

        Arguments:

        - ``x`` -- The horizontal location relative to the room to
          project the dot.
        - ``y`` -- The vertical location relative to the room to project
          the dot.
        - ``z`` -- The Z-axis position of the projection in the room.

        See the documentation for :meth:`sge.Sprite.draw_dot` for more
        information.
        """
        # TODO

    def project_line(self, x1, y1, x2, y2, z, color, thickness=1,
                     anti_alias=False):
        """
        Project a line segment onto the room.

        Arguments:

        - ``x1`` -- The horizontal location relative to the room of the
          first endpoint of the projected line segment.
        - ``y1`` -- The vertical location relative to the room of the
          first endpoint of the projected line segment.
        - ``x2`` -- The horizontal location relative to the room of the
          second endpoint of the projected line segment.
        - ``y2`` -- The vertical location relative to the room of the
          second endpoint of the projected line segment.
        - ``z`` -- The Z-axis position of the projection in the room.

        See the documentation for :meth:`sge.Sprite.draw_line` for more
        information.
        """
        # TODO

    def project_rectangle(self, x, y, z, width, height, fill=None,
                          outline=None, outline_thickness=1):
        """
        Project a rectangle onto the room.

        Arguments:

        - ``x`` -- The horizontal location relative to the room to
          project the rectangle.
        - ``y`` -- The vertical location relative to the room to project
          the rectangle.
        - ``z`` -- The Z-axis position of the projection in the room.

        See the documentation for :meth:`sge.Sprite.draw_rectangle` for
        more information.
        """
        # TODO

    def project_ellipse(self, x, y, z, width, height, fill=None,
                        outline=None, outline_thickness=1, anti_alias=False):
        """
        Project an ellipse onto the room.

        Arguments:

        - ``x`` -- The horizontal location relative to the room to
          position the imaginary rectangle containing the ellipse.
        - ``y`` -- The vertical location relative to the room to
          position the imaginary rectangle containing the ellipse.
        - ``z`` -- The Z-axis position of the projection in the room.
        - ``width`` -- The width of the ellipse.
        - ``height`` -- The height of the ellipse.
        - ``outline_thickness`` -- The thickness of the outline of the
          ellipse.
        - ``anti_alias`` -- Whether or not anti-aliasing should be used.

        See the documentation for :meth:`sge.Sprite.draw_ellipse` for
        more information.
        """
        # TODO

    def project_circle(self, x, y, z, radius, fill=None, outline=None,
                       outline_thickness=1, anti_alias=False):
        """
        Project a circle onto the room.

        Arguments:

        - ``x`` -- The horizontal location relative to the room to
          position the center of the circle.
        - ``y`` -- The vertical location relative to the room to
          position the center of the circle.
        - ``z`` -- The Z-axis position of the projection in the room.

        See the documentation for :meth:`sge.Sprite.draw_circle` for
        more information.
        """
        # TODO

    def project_polygon(self, points, z, fill=None, outline=None,
                        outline_thickness=1, anti_alias=False):
        """
        Draw a polygon on the sprite.

        Arguments:

        - ``points`` -- A list of points relative to the room to
          position each of the polygon's angles.  Each point should be a
          tuple in the form ``(x, y)``, where x is the horizontal
          location and y is the vertical location.
        - ``z`` -- The Z-axis position of the projection in the room.

        See the documentation for :meth:`sge.Sprite.draw_polygon` for
        more information.
        """
        # TODO

    def project_sprite(self, sprite, image, x, y, z, blend_mode=None):
        """
        Project a sprite onto the room.

        Arguments:

        - ``x`` -- The horizontal location relative to the room to
          project ``sprite``.
        - ``y`` -- The vertical location relative to the room to project
          ``sprite``.
        - ``z`` -- The Z-axis position of the projection in the room.

        See the documentation for :meth:`sge.Sprite.draw_sprite` for
        more information.
        """
        # TODO

    def project_text(self, font, text, x, y, z, width=None, height=None,
                    color=sge.Color("black"), halign="left",
                    valign="top", anti_alias=True):
        """
        Project text onto the room.

        Arguments:

        - ``x`` -- The horizontal location relative to the room to
          project the text.
        - ``y`` -- The vertical location relative to the room to project
          the text.
        - ``z`` -- The Z-axis position of the projection in the room.

        See the documentation for :meth:`sge.Sprite.draw_text` for more
        information.
        """
        # TODO

    def event_room_start(self):
        """
        Called when the room is started for the first time.  It is
        always called after any :meth:`sge.Game.event_game_start` and
        before any :class:`sge.Object.event_create` occurring at the
        same time.
        """
        pass

    def event_room_resume(self):
        """
        Called when the room is started after it has already previously
        been started.  It is always called before any
        :meth:`sge.Object.event_create` occurring at the same time.
        """
        pass

    def event_room_end(self):
        """
        Called when another room is started or the game ends while this
        room is the current room.  It is always called before any
        :meth:`sge.Game.event_game_end` occurring at the same time.
        """
        pass

    def event_step(self, time_passed, delta_mult):
        """
        See the documentation for :meth:`sge.Game.event_step` for more
        information.
        """
        pass

    def event_alarm(self, alarm_id):
        """
        See the documentation for :attr:`sge.Room.alarms` for more
        information.
        """
        pass

    def event_key_press(self, key, char):
        """
        See the documentation for :class:`sge.input.KeyPress` for more
        information.
        """
        pass

    def event_key_release(self, key):
        """
        See the documentation for :class:`sge.input.KeyRelease` for more
        information.
        """
        pass

    def event_mouse_move(self, x, y):
        """
        See the documentation for :class:`sge.input.MouseMove` for more
        information.
        """
        pass

    def event_mouse_button_press(self, button):
        """Mouse button press event.

        See the documentation for :class:`sge.input.MouseButtonPress`
        for more information.

        """
        pass

    def event_mouse_button_release(self, button):
        """
        See the documentation for :class:`sge.input.MouseButtonRelease`
        for more information.
        """
        pass

    def event_joystick_axis_move(self, js_name, js_id, axis, value):
        """
        See the documentation for :class:`sge.input.JoystickAxisMove`
        for more information.
        """
        pass

    def event_joystick_hat_move(self, js_name, js_id, hat, x, y):
        """
        See the documentation for :class:`sge.input.JoystickHatMove` for
        more information.
        """
        pass

    def event_joystick_trackball_move(self, js_name, js_id, ball, x, y):
        """
        See the documentation for
        :class:`sge.input.JoystickTrackballMove` for more information.
        """
        pass

    def event_joystick_button_press(self, js_name, js_id, button):
        """
        See the documentation for :class:`sge.input.JoystickButtonPress`
        for more information.
        """
        pass

    def event_joystick_button_release(self, js_name, js_id, button):
        """
        See the documentation for
        :class:`sge.input.JoystickButtonRelease` for more information.
        """
        pass

    def event_gain_keyboard_focus(self):
        """
        See the documentation for :class:`sge.input.KeyboardFocusGain`
        for more information.
        """
        pass

    def event_lose_keyboard_focus(self):
        """
        See the documentation for :class:`sge.input.KeyboardFocusLose`
        for more information.
        """
        pass

    def event_gain_mouse_focus(self):
        """
        See the documentation for :class:`sge.input.MouseFocusGain` for
        more information.
        """
        pass

    def event_lose_mouse_focus(self):
        """
        See the documentation for :class:`sge.input.MouseFocusLose` for
        more information.
        """
        pass

    def event_close(self):
        """
        This is always called before any :meth:`sge.Game.event_close`
        occurring at the same time.

        See the documentation for :class:`sge.input.QuitRequest` for
        more information.
        """
        pass

    def event_paused_step(self, time_passed, delta_mult):
        """
        See the documentation for :meth:`sge.Game.event_step` for more
        information.
        """
        pass

    def event_paused_key_press(self, key, char):
        """
        See the documentation for :class:`sge.input.KeyPress` for more
        information.
        """
        pass

    def event_paused_key_release(self, key):
        """
        See the documentation for :class:`sge.input.KeyRelease` for more
        information.
        """
        pass

    def event_paused_mouse_move(self, x, y):
        """
        See the documentation for :class:`sge.input.MouseMove` for more
        information.
        """
        pass

    def event_paused_mouse_button_press(self, button):
        """
        See the documentation for :class:`sge.input.MouseButtonPress`
        for more information.
        """
        pass

    def event_paused_mouse_button_release(self, button):
        """
        See the documentation for :class:`sge.input.MouseButtonRelease`
        for more information.
        """
        pass

    def event_paused_joystick_axis_move(self, js_name, js_id, axis, value):
        """
        See the documentation for :class:`sge.input.JoystickAxisMove`
        for more information.
        """
        pass

    def event_paused_joystick_hat_move(self, js_name, js_id, hat, x, y):
        """
        See the documentation for :class:`sge.input.JoystickHatMove` for
        more information.
        """
        pass

    def event_paused_joystick_trackball_move(self, js_name, js_id, ball, x, y):
        """
        See the documentation for
        :class:`sge.input.JoystickTrackballMove` for more information.
        """
        pass

    def event_paused_joystick_button_press(self, js_name, js_id, button):
        """
        See the documentation for :class:`sge.input.JoystickButtonPress`
        for more information.
        """
        pass

    def event_paused_joystick_button_release(self, js_name, js_id, button):
        """
        See the documentation for
        :class:`sge.input.JoystickButtonRelease` for more information.
        """
        pass

    def event_paused_gain_keyboard_focus(self):
        """
        See the documentation for :class:`sge.input.KeyboardFocusGain`
        for more information.
        """
        pass

    def event_paused_lose_keyboard_focus(self):
        """
        See the documentation for :class:`sge.input.KeyboardFocusLose`
        for more information.
        """
        pass

    def event_paused_gain_mouse_focus(self):
        """
        See the documentation for :class:`sge.input.MouseFocusGain` for
        more information.
        """
        pass

    def event_paused_lose_mouse_focus(self):
        """
        See the documentation for :class:`sge.input.MouseFocusLose` for
        more information.
        """
        pass

    def event_paused_close(self):
        """
        See the documentation for :meth:`sge.Room.event_close` for more
        information.
        """
        pass
