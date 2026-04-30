import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

class vehicle:
    def __init__(self, initial_state, mass, epoch):

        self.ref_state = initial_state
        self.m = mass
        self.state = initial_state
        self.t0 = epoch #posix time

    def getForces():
        #use analytical models of n-body gravitation, j2 perturbation, srp force, drag to calculate forces in the RIC frame
         


        f = f_nbody + f_j2 + f_srp + f_drag

        return f

    def getXDot():
        
        f = vehicle.getForces()
        #pass in RIC frame forces and calculate beta_dot, transform to j2000, calculate state derivative vector for propogation
        return XDot  
    
    def autoDiff():
        #use the current state alongside the state propogated for the next timestep to populate the A matrix for BLS stuff
        
        return A_mat
     

class celes_body:
    def __init__(self,COE,epoch,mass,radius):
        self.coe = COE
        self.t0 = epoch
        self.m = mass
        self.r = radius
    def getState():
        #return the j2000 state of celestial body
        return state




