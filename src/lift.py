from typing import List
from enums.lift import LiftStatus, Direction


# class LiftPanel:
#     def __init__(self, active_floors: list, total_floor: list):
#         self.total_floor = total_floor
#         self.active_floors = active_floors
#         self.selected_floor = [False for _ in range(len(total_floor))]


class Lift:
    def __init__(
        self,
        lift_num: int,
        running_status: LiftStatus = LiftStatus.stop,
        running_direction: Direction = Direction.idle,
        time_between_floor: int = 15,
        waiting_time: int = 30,
        current_floor: int = 0,
        max_capacity: int = 50,
        current_capacity: int = 0,
        total_floor: int = 0,
        active_floors: List[int] = None
    ):
        self.lift_num = lift_num
        # self.accessible_floor = accessible_floor
        self.running_status = running_status
        self.running_direction = running_direction
        # self.stoppage = stoppage
        self.time_between_floor = time_between_floor
        self.waiting_time = waiting_time
        self.current_floor = current_floor
        self.max_capacity = max_capacity
        self.current_capacity = current_capacity
        self.total_floor = total_floor
        self.active_floors = active_floors
        self.selected_floor = [False for _ in range(total_floor)]

    def select_floor(self, floor: int) -> bool:
        if floor in self.active_floors:
            if self.selected_floor[floor]:
                return True
            self.selected_floor[floor] = True
        return False

    def set_direction(self, direction: Direction):
        self.running_direction = direction

    def get_direction(self):
        return self.running_direction

    def get_next_stop(self):
        for idx in range(len(self.selected_floor)):
            if self.selected_floor[idx]:
                if (
                        self.running_direction == Direction.up and
                        idx > self.current_floor
                ):
                    return idx
                elif(
                        self.running_direction == Direction.down and
                        idx > self.current_floor
                ):
                    return idx-1
        return self.current_floor

    def arrived_floor(self, floor):
        self.selected_floor[floor] = False

    def calculate_cost(self, selected_floor):
        pass


class Person:
    pass


class Floor:
    pass


class Door:
    pass


class Button:
    def __init__(self):
        self.state = False

    def set_on(self):
        self.state = True

    def set_off(self):
        self.state = False

    def get_state(self):
        return self.state


class FloorButton:
    def __init__(self):
        self.up = Button
        self.down = Button
