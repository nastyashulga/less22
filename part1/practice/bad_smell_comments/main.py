# В данном коде все прокомментировано как надо,
# но слишком избыточно.
# Избавьтесь от комментариев, изменив имена переменных, 
# чтобы было понятно, за что эти переменные отвечают 
# и что происходит и без комментариев


class Unit:
    def unit_movement(self, field, field_x: int, field_y: int, direction, is_fly: bool, creep: bool, speed=1):
        """Функция реализует перемещение юнита по полю. в качестве параметров принимает текущие координаты юнита, 
        направление его движения, состояние не летит ли он, состояние не крадется ли он и базовый параметр скорости с 
        которым двигается юнит
        """
        if is_fly and creep:
            raise ValueError('Рожденный ползать летать не должен!')

        if is_fly:
            speed *= 1.2
            if direction == 'UP':
                new_y = field_y + speed
                new_x = field_x
            elif direction == 'DOWN':
                new_y = field_y - speed
                new_x = field_x
            elif direction == 'LEFT':
                new_y = field_y
                new_x = field_x - speed
            elif direction == 'RIGHT':
                new_y = field_y
                new_x = field_x + speed
        if creep:
            speed *= 0.5
            if direction == 'UP':
                new_y = field_y + speed
                new_x = field_x
            elif direction == 'DOWN':
                new_y = field_y - speed
                new_x = field_x
            elif direction == 'LEFT':
                new_y = field_y
                new_x = field_x - speed
            elif direction == 'RIGHT':
                new_y = field_y
                new_x = field_x + speed

            field.set_unit(x=new_x, y=new_y, unit=self)

