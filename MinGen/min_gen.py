from MinGen.dataclasses import PromRow


class MinGen:
    def __init__(self, signs_count, objects_count, data):
        self.signs_count = signs_count
        self.objects_count = objects_count
        self.data = data
        self.prom_tab = self._make_prom_tab()

    def print_data(self):
        print(' '.join(self.chars))
        for i in range(self.objects_count):
            print(' '.join([str(j) for j in self.data[i]]))

    def print_prom_tab(self):
        print('      '.join(['X', 'K', 'X\'' + ' ' * (self.objects_count - 2), 'X"']))
        for prom_row in self.prom_tab:
            print('      '.join([
                prom_row.X_name,
                '+' if prom_row.Key else '-',
                ''.join([str(i+1) for i in prom_row.X_1]) +
                ' ' * (self.objects_count - len(prom_row.X_1)),
                prom_row.X_2,
            ]))

    def _intersect(self, lst):
        if not lst:
            return [1] * self.signs_count
        res = []
        for i in range(len(lst[0])):
            if sum([lst[j][i] for j in range(len(lst))]) == len(lst):
                res.append(1)
            else:
                res.append(0)
        return res

    def _list_from_chars(self, chars):
        res = []
        for i in range(self.signs_count):
            if self.chars[i] in chars:
                res.append(1)
            else:
                res.append(0)
        return res

    def _chars_from_list(self, lst):
        res = ""
        for i in range(len(lst)):
            if lst[i]:
                res += self.chars[i]
        return res

    def _get_objects_by_sign(self, i):
        objects = []
        for j in range(len(self.data)):
            if self.data[j][i]:
                objects.append(j)
        return objects

    def _get_objects_by_char(self, char):
        index = self.chars.index(char)
        return self._get_objects_by_sign(index)

    def _get_x_2_lst_from_objects(self, objects):
        obj_lists = [self.data[i] for i in range(self.objects_count) if i in objects]
        x_2_lst = self._intersect(obj_lists)
        return x_2_lst

    @property
    def chars(self):
        return [chr(ord('A') + i) for i in range(self.signs_count)]

    def _make_prom_tab(self):
        prom_tab = []
        for char in self.chars:
            lst = self._list_from_chars(char)
            x_1 = self._get_objects_by_char(char)
            x_2_lst = self._get_x_2_lst_from_objects(x_1)
            x_2 = self._chars_from_list(x_2_lst)
            prom_tab.append(PromRow(char, lst, True, x_2, x_1, x_2, x_2_lst))
        return prom_tab
