#Author: Lennaert van Veen
#Date: 1/17/2019
# Python function that computes the distance travelled by a cannon ball with air friction.
# In: theta, angle of the shot; c, coefficient of air friction;
# g, accelleration of gravity; V0, initial speed. See lecture 2.
# A solution of dist=R is the angle at which to tilt the canon for given c, g and V0.
import math

def dist(theta,c,g,V0):
    return (1/c) * math.log((c*V0*math.cos(theta)/math.sqrt(c*g)) *                    \
                       (math.atan(math.sqrt(c/g)*V0*math.sin(theta)) +                 \
                        math.acosh(math.sqrt((g+c* V0**2 * math.sin(theta)**2)/g)))+1.0)


