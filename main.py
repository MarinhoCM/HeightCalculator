class HeightCalculator:
    def __init__(self: object, num_people: int) -> None:
        self.__num_people = num_people
        self.__heights = []

    @property
    def num_people(self: object) -> int:
        return self.__num_people
    
    @property
    def heights(self: object) -> list:
        return self.__heights
    
    def collect_heights(self) -> None:
        try:
            for i in range(self.num_people):
                while True:
                    try:
                        height = float(input(
                                f"Informe a altura da pessoa {i + 1}: "
                            )
                        )
                        if height > 0:
                            self.heights.append(height)
                            break
                        else:
                            print(
                                "Por favor, informe uma" \
                                " altura válida e positiva."
                            )
                    except ValueError:
                        print(
                            "Por favor, informe um número" \
                            " válido para a altura."
                        )
        except KeyboardInterrupt:
            print("\n"+40*"--")

    def calculate_statistics(self) -> None:
        if not self.heights:
            print("Nenhuma altura fornecida.")
            return

        max_height = max(self.heights)
        min_height = min(self.heights)
        average_height = sum(self.heights) / len(self.heights)

        print(f"\naltura máxima: {max_height}")
        print(f"altura mínima: {min_height}")
        print(f"altura média: {average_height}")

        below_average_count = sum(
            height < average_height for height in self.heights
        )
        print(f"Pessoas com altura abaixo da média: {below_average_count}")
        
    def __str__(self) -> str:
        return (
            """\t\tConsidere a realização de uma pesquisa com 1 000
                pessoas para obtenção das seguintes informações:
                   o valor da maior height; o valor da menor height;
                   a média das heights; 
                   quantas pessoas têm height inferior à média das heights.

                Considere, ainda, que um programador foi selecionado para
                desenvolver um modelo de código que soluciona o problema 
                automatizando (Exemplo:Utilizando Estrutura de Repetição)
                a coleta das heights e a geração das informações. 

                Com base nas informações apresentadas, desenvolva o código
                adequado para resolver o problema usando qualquer linguagem
                de programação"""
            )

    
if __name__ == "__main__":
    num_people = 1000 
    print(calculator := HeightCalculator(num_people))
    calculator.collect_heights()
    calculator.calculate_statistics()
    