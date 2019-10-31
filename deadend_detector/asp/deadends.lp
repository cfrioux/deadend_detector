% reaction("r1").
% reaction("r2").
% reactant("A","r1").
% product("B","r1").
% reactant("B","r2").
% product("C","r2").

deadend_np(M) :- reaction(R), reactant(M,R), not product(M,R2):reaction(R2).
deadend_nc(M) :- reaction(R), product(M,R), not reactant(M,R2):reaction(R2).

#show deadend_np/1.
#show deadend_nc/1.