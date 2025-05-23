/* The code is a brute force implementation and will stagnate at 0.35 score. Convergence time is astronomically high. */

#include <iostream>
#include <random>

std::string generate(int target_length, std::mt19937 &gen) {
    // Generate a random lowercase string of size length
    
    std::string choices = "abcdefghijklmnopqrstuvwxyz ";
    int choice_pool = choices.length();
    // the range from of choices (indices)
    std::uniform_int_distribution<> dis(0, choice_pool-1);

    // generate a random string of same size as target
    std::string generation = "";
    for (int i = 0; i < target_length; i++) {
        // increment a random letter
        char rnd_letter = choices[dis(gen)];
        generation += rnd_letter;
    }

    return generation;
}


double similarity_score(std::string str1, std::string str2) {
    // compute similarity score between 2 strings of same length (exact matching)

    int length = str1.length();
    double score = 0;
    
    for (int i = 0; i < length; i++) {
        
        if (str1[i] == str2[i]) {
            score += 1.0 / length;
        } 

    }

    return score;
}

int main() {

    std::cout << std::endl;

    // initialize a random engine for choosing a random letter (via index)
    std::random_device rd; 
    std::mt19937 gen(rd());

    std::string target = "methinks it is like a weasel";
    std::string best_gen_so_far = "";
    double score = 0, max_score = 0;
    

    // iterate until the target is generated
    int k = 0;
    while (max_score < 1) {
        // pass the random engine (by reference, so its internal state is tracked) and the target length for generation
        std::string generated = generate(target.length(), gen);
        score = similarity_score(generated, target);
        if (score > max_score) {
            max_score = score;
            best_gen_so_far = generated;
        }

        k += 1;
        if (!(k%10000000)) {
            std::cout << "Best score so far after " << k/1000000 << " million iterations: " << max_score << std::endl;
            std::cout << "Best generation so far: " << best_gen_so_far << std::endl << std::endl;
        } 
    } 

    std::cout << "The target string was successfully generated after " << k << " iterations.";

}