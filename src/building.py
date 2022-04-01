from lift import Lift
from enums.lift import Direction


class ElevatorSystem:
    def __init__(
            self,
            system_num: int,
            floors: int,
            active_floors: list,
    ):
        self.system_num = system_num
        self.elevators = list()
        self.elevator_num = 0
        self.floors = floors
        self.active_floors = active_floors

    @staticmethod
    def calculate_cost(elev, floor):
        cost = 0
        curr = elev.current_floor
        direction = elev.running_direction
        while curr != floor:
            # If left reached to bottom or top change the direction towards
            # required floor
            if curr == elev.total_floor or curr == 0:
                direction = Direction.up if curr < floor else Direction.down
            # if lift moving upwards
            if direction == Direction.up:
                curr += 1
            # If lift Moving downwards
            if direction == Direction.down:
                curr -= 1
            # If lift is in idle state
            if direction == Direction.idle:
                direction = Direction.up if curr < floor else Direction.down
            # Add time to reached to next level
            cost += elev.time_between_floor
            # If the floor have stoppage
            if elev.selected_floor:
                # Add the waiting time of the floor
                cost += elev.waiting_time
        return cost

    def get_selected_lift(self, lift, cost, elev, floor):
        if not lift:
            return elev, self.calculate_cost(elev, floor)
        else:
            temp_cost = self.calculate_cost(elev, floor)
            if temp_cost < cost:
                return elev, self.calculate_cost(elev, floor)

    def get_lift(self, floor, direction):
        assign_elevator = None
        same_direction_lift = None
        same_direction_cost = -1
        idle_lift = None
        idle_lift_cost = -1
        opp_direction_lift = None
        opp_direction_cost = -1
        for elev in self.elevators:
            if elev.running_direction == direction:
                same_direction_lift, same_direction_cost = self.get_selected_lift(
                    same_direction_lift,
                    same_direction_cost,
                    elev,
                    floor,
                )
            elif elev.running_direction == Direction.idle:
                idle_lift, idle_lift_cost = self.get_selected_lift(
                    idle_lift,
                    idle_lift_cost,
                    elev,
                    floor,
                )
            else:
                opp_direction_lift, opp_direction_cost = self.get_selected_lift(
                    opp_direction_lift,
                    opp_direction_cost,
                    elev,
                    floor,
                )

    def create_elevator(
        self,
        active_floors: list,
        max_capacity: int
    ):
        self.elevator_num += 1
        self.elevators.append(
            Lift(
                lift_num=self.elevator_num,
                max_capacity=max_capacity,
                total_floor=self.floors,
                active_floors=active_floors,
            )
        )
