import difflib


class SequenceMatcher(object):
    def __init__(self, reserved, *args):
        assert reserved is None
        self.__combined = []
        self.__lines = []
        self.__size = 0
        for index, i in enumerate(args):
            self._merge(i, index)

    def _copy_set_list(self, set_list):
        return list(map(set, set_list))

    def _merge(self, l, tag):
        diff = difflib.SequenceMatcher(None, self.__combined, l)
        new_combined = []
        new_lines = []
        for action, lhs_begin, lhs_end, rhs_begin, rhs_end in diff.get_opcodes():
            new_combined.extend(self.__combined[lhs_begin:lhs_end])
            new_lines.extend(self._copy_set_list(self.__lines[lhs_begin:lhs_end]))
            if action == 'equal':
                for i in range(0, rhs_end-rhs_begin):
                    new_lines[-1-i].add(tag)
            else:
                new_combined.extend(l[rhs_begin:rhs_end])
                new_lines.extend([set([tag])] * (rhs_end - rhs_begin))
        self.__combined = new_combined
        self.__lines = new_lines
        self.__size += 1

    def get_opcodes(self):
        opcodes = []
        indices = []
        for i in range(0, self.__size):
            indices.append(0)
        last_set = None
        begins = list(indices)
        for line in self.__lines:
            if not last_set is None and line != last_set:
                opcodes.append((action, begins, list(indices)))
                begins = list(indices)
            if len(line) == self.__size:
                action = 'equal'
            else:
                action = 'complicated'
            for i in range(0, self.__size):
                if i in line:
                    indices[i] += 1
            last_set = line
        if begins != indices:
            opcodes.append((action, begins, indices))
        return opcodes
