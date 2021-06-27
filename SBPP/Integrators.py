#from numba import jit,njit 
from SBPP import *
@njit
def Integrator_nonRel(q0,dq0,E_func,B_func,masses,charges,dt,tf,fparams1,debug=False,output_Freq = 1):
    t = 0
    qs=[]
    q0,dqm1b2 = jumpstart_push_nonRel(q0,dq0,E_func,B_func,masses,charges,dt,0,fparams=fparams1)
    q_n = q0
    #print(q_n)
    #print(dqm1b2)
    dq_n = dqm1b2
    qs.append(q_n)
    ctr = 0
    while t < tf:
        q_n, dq_n = Boris_Push(q_n,dq_n,E_func,B_func,charges,masses,dt,t,fparams=fparams1,debug = debug)
        #print(dq_n)
        if ctr == output_Freq:
            qs.append(q_n)
            ctr = 0
        t+=dt
    #print(t)
    return (qs,dq_n)
@njit
def Integrator_Rel(q0,dq0,E_func,B_func,masses,charges,dt,tf,fparams1,debug=False,output_Freq = 1):
    t = 0
    qs=[]
    q0,dqm1b2 = jumpstart_push_Rel(q0,dq0,E_func=E_func_zero,B_func=B_func_Uniform_z,mass=masses,charge=charges,dt=1e-9,t=0,fparams=fparams_gyration)
    q_n = q0
    #print(q_n)
    #print(dqm1b2)
    dq_n = dqm1b2
    qs.append(q_n)
    ctr = 0
    while t < tf:
        q_n, dq_n = Boris_Push_Rel(q_n,dq_n,E_func,B_func,charges,masses,dt,t,fparams=fparams1,debug = debug)
        #print(dq_n)
        if ctr == output_Freq:
            qs.append(q_n)
            ctr = 0
        t+=dt
    #print(t)
    return (qs,dq_n)
#@njit
def Integrator_Synched(q0,dq0,E_func,B_func,masses,charges,dt,tf,fparams1,debug=False,gamma_specified = 0,output_Freq = 1):
    t= 0
    qs = []
    dqs = []
    ts=[]
    ts.append(t)
    qs.append(q0)
    dqs.append(dq0)
    q_n = q0
    dq_n = dq0
    ctr = 0
    while t<tf:
        q_n,dq_n =Boris_Push_Relativistic_Synced(q_n,dq_n,E_func,B_func,charges,masses,dt,t,fparams=fparams1,gamma_specified=gamma_specified)
        if ctr == output_Freq:
            qs.append(q_n)
            dqs.append(dq_n)
            ctr = 0
        t+=dt
        ts.append(t)
    return (qs,dqs)
    
@njit
def Integrator_Synched_nonRel(q0,dq0,E_func,B_func,masses,charges,dt,tf,fparams1,debug=False,gamma_specified=0,output_Freq = 1):
    t= 0
    qs = []
    ts = []
    dqs = []
    qs.append(q0)
    dqs.append(dq0)
    q_n = q0
    dq_n = dq0
    ctr = 0
    ts.append(t)
    while t<tf:
        ctr+=1
        q_n,dq_n = Boris_Push_Synchronized(q_n,dq_n,E_func,B_func,charges,masses,
                                                  dt,t,fparams=fparams1,gamma_specified=gamma_specified,debug=debug)
        if(ctr==output_Freq):
            qs.append(q_n)
            dqs.append(dq_n)
            ctr = 0
        t+=dt
        ts.append(t)
    return (qs,dqs,ts)
def Integrator_Synched_nonRel_Experimental(q0,dq0,E_func,B_func,masses,charges,dt,tf,fparams1,debug=False,gamma_specified=0,output_Freq = 1):
    t= 0
    qs = []
    dqs = []
    qs.append(q0)
    dqs.append(dq0)
    q_n = q0
    dq_n = dq0
    ctr = 0
    while t<tf:
        ctr+=1
        q_n,dq_n = Boris_Push_Synchronized_Superfast(q_n,dq_n,E_func,B_func,charges,masses,
                                                  dt,t,fparams=fparams1,gamma_specified=gamma_specified)
        if(ctr==output_Freq):
            qs.append(q_n)
            dqs.append(dq_n)
            ctr = 0
        t+=dt
    return (qs,dqs)