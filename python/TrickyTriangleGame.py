#partially based on https://keras.io/examples/rl/actor_critic_cartpole/

import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

class Peg():
    def __init__(self, id):
        self.id = id

class Hole():
    def __init__(self, id):
        self.id = id
        self.adjacents = []
        self.peg = None

    def add_adjacent(self, other):
        self.adjacents.append(other)

    def add_line(self, line):
        self.lines.append(line)

    def insert_peg(self, peg):
        if self.peg is None:
            self.peg = peg
            return True
        else: 
            return False

class Board:
    def peg_in(self, peg, hole):
        if self.holes[hole.peg.id].id is peg.id:
            return True
        else:
            return False

    def peg_exists(self, peg):
        for h in self.holes:
            if h.peg is not None and peg is not None:
                if h.peg.id is peg.id:
                    return True
        return False

    def hole_empty(self, hole):
        if self.holes[hole.id].peg is None:
            return True
        else:
            return False

    def check_if_move_allowed(self, peg, source_hole, over_hole, destination_hole):
        if self.peg_exists(peg) and self.peg_in(peg, source_hole) and not self.hole_empty(over_hole) and self.hole_empty(destination_hole) and ([source_hole, over_hole, destination_hole] in self.lines):
           return True
        else:
            return False

    #method to detect if legal moves are present on the board
    def legal_moves(self):
        legal_moves = list()
        for h in self.holes:
            if h.peg is not None:
                for over in h.adjacents:
                    for dest in over.adjacents:
                        if over is not dest and h is not over and h is not dest:
                            if self.check_if_move_allowed(h.peg, h, over, dest):
                                #print("peg"+str(h.peg.id)+" source"+str(h.id)+" over"+str(over.id)+" dest"+str(dest.id))
                                legal_moves.append([h.peg, h, over, dest])
        return legal_moves

    def move_peg(self, peg, source_hole, over_hole, destination_hole):
        if self.check_if_move_allowed(peg, source_hole, over_hole, destination_hole):
            self.remove_peg(over_hole)
            peg_to_insert = self.remove_peg(source_hole)
            self.insert_peg(peg_to_insert, destination_hole)

    def remove_peg(self, hole):
        peg = self.holes[hole.id].peg
        self.holes[hole.id].peg = None
        self.number_of_pegs = self.number_of_pegs - 1
        return peg

    def insert_peg(self, peg, hole):
        self.holes[hole.id].peg = peg
        self.number_of_pegs = self.number_of_pegs + 1

    def reset(self):
        self.holes = []
        self.levels = []
        self.lines = []
        
        self.number_of_pegs = 0
        level_count = 0
        for i in range(self.num_levels):
            level_count = level_count + 1
            self.levels.append(level_count)

        hole_count = 0
        for level in self.levels:
            for spot in range(level):
                self.holes.append(Hole(hole_count))
                hole_count = hole_count +1

        self.holes[0].add_adjacent(self.holes[1])
        self.holes[0].add_adjacent(self.holes[2])

        self.holes[1].add_adjacent(self.holes[0])
        self.holes[1].add_adjacent(self.holes[2])
        self.holes[1].add_adjacent(self.holes[3])
        self.holes[1].add_adjacent(self.holes[4])

        self.holes[2].add_adjacent(self.holes[0])
        self.holes[2].add_adjacent(self.holes[1])
        self.holes[2].add_adjacent(self.holes[4])
        self.holes[2].add_adjacent(self.holes[5])

        self.holes[3].add_adjacent(self.holes[1])
        self.holes[3].add_adjacent(self.holes[4])
        self.holes[3].add_adjacent(self.holes[6])
        self.holes[3].add_adjacent(self.holes[7])

        self.holes[4].add_adjacent(self.holes[1])
        self.holes[4].add_adjacent(self.holes[2])
        self.holes[4].add_adjacent(self.holes[3])
        self.holes[4].add_adjacent(self.holes[5])
        self.holes[4].add_adjacent(self.holes[7])
        self.holes[4].add_adjacent(self.holes[8])

        self.holes[5].add_adjacent(self.holes[2])
        self.holes[5].add_adjacent(self.holes[4])
        self.holes[5].add_adjacent(self.holes[8])
        self.holes[5].add_adjacent(self.holes[9])
        self.holes[5].add_adjacent(self.holes[7])

        self.holes[6].add_adjacent(self.holes[3])
        self.holes[6].add_adjacent(self.holes[7])

        self.holes[7].add_adjacent(self.holes[3])
        self.holes[7].add_adjacent(self.holes[4])
        self.holes[7].add_adjacent(self.holes[7])
        self.holes[7].add_adjacent(self.holes[8])

        self.holes[8].add_adjacent(self.holes[4])
        self.holes[8].add_adjacent(self.holes[5])
        self.holes[8].add_adjacent(self.holes[7])
        self.holes[8].add_adjacent(self.holes[9])

        self.holes[9].add_adjacent(self.holes[5])
        self.holes[9].add_adjacent(self.holes[8])

        #    0
        #   1 2
        #  3 4 5
        # 6 7 8 9

        self.lines.append([self.holes[0],self.holes[1], self.holes[3]])
        self.lines.append([self.holes[0],self.holes[2], self.holes[5]])

        self.lines.append([self.holes[1],self.holes[3], self.holes[6]])
        self.lines.append([self.holes[1],self.holes[4], self.holes[8]])

        self.lines.append([self.holes[2],self.holes[4], self.holes[7]])
        self.lines.append([self.holes[2],self.holes[5], self.holes[9]])
        
        self.lines.append([self.holes[3],self.holes[1], self.holes[0]])
        self.lines.append([self.holes[3],self.holes[4], self.holes[5]])

        self.lines.append([self.holes[5],self.holes[2], self.holes[0]])
        self.lines.append([self.holes[5],self.holes[4], self.holes[3]])

        self.lines.append([self.holes[6],self.holes[3], self.holes[1]])
        self.lines.append([self.holes[6],self.holes[7], self.holes[8]])

        self.lines.append([self.holes[7],self.holes[4], self.holes[2]])
        self.lines.append([self.holes[7],self.holes[8], self.holes[9]])

        self.lines.append([self.holes[8],self.holes[4], self.holes[1]])
        self.lines.append([self.holes[8],self.holes[7], self.holes[6]])

        self.lines.append([self.holes[9],self.holes[5], self.holes[2]])
        self.lines.append([self.holes[9],self.holes[8], self.holes[7]])

        count = 0
        for location in self.holes:
            location.insert_peg(Peg(count))
            count = count +1
            self.number_of_pegs = self.number_of_pegs+1

        self.remove_peg(self.holes[2])
        state = list()
        for h in self.holes:
            if self.hole_empty(h):
                state.append(0)
            else:
                state.append(1)
        return state
    
    def get_state(self):
        state = list()
        for h in self.holes:
            if self.hole_empty(h):
                state.append(0)
            else:
                state.append(1)
        return state

    def step(self, action):
        move = self.lines[action] #self.holes[x],self.holes[y], self.holes[z]
        peg = move[0].peg
        source = move[0]
        over = move[1]
        dest = move[2]
        if self.check_if_move_allowed(peg, source, over, dest):
            self.move_peg(peg, source, over, dest)
            if len(self.legal_moves()) == 0:
                if self.number_of_pegs == 1:
                    print("sucess")
                    reward = +10.0
                    done = True
                elif self.number_of_pegs == 2:
                    print("two remained")
                    done = True
                    reward = 2.0
                elif self.number_of_pegs == 3:
                    print("three remained")
                    done = True
                    reward = 1.0
                else:
                    done = True
                    reward = -10.0
            else:
                reward = +0.5
                done = False
        else:
            if len(self.legal_moves()) == 0:
                done = True
                reward = -10.0
            else:
                reward = -0.5
                done = False
        return self.get_state(), reward, done, {}
    

    def __init__(self, num_levels):
        self.num_levels = num_levels
        self.reset()
       

class Actor():
    pass

class Critic():
    pass
        

if __name__ == "__main__":
    game = Board(4)

    #actor critic model
    # Configuration parameters for the whole setup
    
    gamma = 0.99  # Discount factor for past rewards
    max_steps_per_episode = 100
    num_inputs = len(game.holes)
    num_actions = len(game.lines)
    eps = np.finfo(np.float32).eps.item()
    
    num_hidden = 128

    inputs = layers.Input(shape=(num_inputs,))
    x = layers.Dense(num_hidden, activation="relu")(inputs)
    common = layers.Dense(num_hidden, activation="relu")(x)
    common = layers.Dense(num_actions, activation="linear")(common)
    action = layers.Dense(num_actions, activation="softmax")(common)
    critic = layers.Dense(1)(common)

    model = keras.Model(inputs=inputs, outputs=[action, critic])
    model.summary()
    optimizer = keras.optimizers.Adam(learning_rate=0.02)
    huber_loss = keras.losses.Huber()
    action_probs_history = []
    critic_value_history = []
    rewards_history = []
    running_reward = 0
    episode_count = 0

    while True:  # Run until solved
        state = game.reset()
        episode_reward = 0
        with tf.GradientTape() as tape:
            for timestep in range(1, max_steps_per_episode):

                state = tf.convert_to_tensor(state)
                state = tf.expand_dims(state, 0)

                # Predict action probabilities and estimated future rewards
                # from environment state
                action_probs, critic_value = model(state)
                critic_value_history.append(critic_value[0, 0])

                # Sample action from action probability distribution
                action = np.random.choice(num_actions, p=np.squeeze(action_probs))
                action_probs_history.append(tf.math.log(action_probs[0, action]))

                # Apply the sampled action in our environment
                state, reward, done, _ = game.step(action)
                rewards_history.append(reward)
                episode_reward += reward

                if done:
                    break

            # Update running reward to check condition for solving
            running_reward = 0.05 * episode_reward + (1 - 0.05) * running_reward

            # Calculate expected value from rewards
            # - At each timestep what was the total reward received after that timestep
            # - Rewards in the past are discounted by multiplying them with gamma
            # - These are the labels for our critic
            returns = []
            discounted_sum = 0
            for r in rewards_history[::-1]:
                discounted_sum = r + gamma * discounted_sum
                returns.insert(0, discounted_sum)

            # Normalize
            returns = np.array(returns)
            returns = (returns - np.mean(returns)) / (np.std(returns) + eps)
            returns = returns.tolist()

            # Calculating loss values to update our network
            history = zip(action_probs_history, critic_value_history, returns)
            actor_losses = []
            critic_losses = []
            for log_prob, value, ret in history:
                # At this point in history, the critic estimated that we would get a
                # total reward = `value` in the future. We took an action with log probability
                # of `log_prob` and ended up recieving a total reward = `ret`.
                # The actor must be updated so that it predicts an action that leads to
                # high rewards (compared to critic's estimate) with high probability.
                diff = ret - value
                actor_losses.append(-log_prob * diff)  # actor loss

                # The critic must be updated so that it predicts a better estimate of
                # the future rewards.
                critic_losses.append(
                    huber_loss(tf.expand_dims(value, 0), tf.expand_dims(ret, 0))
                )

            # Backpropagation
            loss_value = sum(actor_losses) + sum(critic_losses)
            grads = tape.gradient(loss_value, model.trainable_variables)
            optimizer.apply_gradients(zip(grads, model.trainable_variables))

            # Clear the loss and reward history
            action_probs_history.clear()
            critic_value_history.clear()
            rewards_history.clear()

        # Log details
        episode_count += 1
        if episode_count % 100 == 0:
            template = "running reward: {:.2f} at episode {}"
            print(template.format(running_reward, episode_count))