import os

clear = lambda: os.system("cls")


class FiniteStateMachine:
    def __init__(
        self,
        states: list[int],
        alphabet: list[str],
        initial_state: int,
        final_states: list[int],
        transitions: dict[int, dict[str, int]],
    ) -> None:
        self.states = states
        self.alphabet = alphabet
        self.initial_state = initial_state
        self.final_states = final_states
        self.transitions = transitions

    def _try_move_state(self, char: str, state: int) -> tuple[int, bool]:
        if char not in self.alphabet or state not in self.transitions:
            return state, False
        if char not in self.transitions[state]:
            return state, False

        return self.transitions[state][char], True

    def matches(self, string: str) -> list[str]:
        source = string

        matches = []
        match = ""
        last_match = ""

        state = self.initial_state
        i = 0
        while source:
            if i < len(source):
                char = source[i]

                state, moved = self._try_move_state(char, state)
                if moved:
                    match += char
                    i += 1
                    if state in self.final_states:
                        last_match = match
                    continue
                else:
                    if state == self.initial_state:
                        source, i = source.removeprefix(char), 0
                        continue

            matched = match if state in self.final_states else last_match
            if not matched:
                source, i = source.removeprefix(match), 0
            else:
                matches.append(matched)
                source, i = source.removeprefix(matched), 0

            state = self.initial_state
            match = ""
            last_match = ""

        return matches


def main() -> None:
    fsmachine = FiniteStateMachine(
        states=[1, 2, 3, 4, 5, 6],
        alphabet=["a", "b", "c", "d", "e"],
        initial_state=1,
        final_states=[4, 5, 6],
        transitions={
            1: {"b": 2, "a": 6, "d": 3},
            2: {"d": 5},
            3: {"c": 5, "e": 4},
            4: {"d": 3, "b": 2, "e": 4},
            5: {"d": 3, "b": 2},
            6: {"a": 6},
        },
    )

    while True:
        clear()
        string = input("Введите строку:\n")

        matches = fsmachine.matches(string)
        if not matches:
            print("\nНет вхождений...")
        else:
            print("\nВхождения:")
            for i in range(len(matches)):
                print(f'[{i}] "{matches[i]}"')

        input()


if __name__ == "__main__":
    main()
