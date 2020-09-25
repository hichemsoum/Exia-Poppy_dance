import move
from pypot.creatures import PoppyErgoJr

poppy = PoppyErgoJr(simulator='vrep', scene='poppy_ergo_jr_holder.ttt', camera='dummy')
move.rest_pose(poppy,3)
move.little_dance(poppy)