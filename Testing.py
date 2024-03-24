import methods
import mutation_llms
import sememe_coref


# Generate mutants for atomic gender mutation
ex1 = mutation_llms.mutation(["The man.", "The black man."], "data/gender/male_female.csv")

# Generate mutants for intersectional race and gender mutation
ex2 = (mutation_llms.mutation(["The man.", "The black man."], "data/race/minority_majority.csv", "data/gender/male_female.csv"))