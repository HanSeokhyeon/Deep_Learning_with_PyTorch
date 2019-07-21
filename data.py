import torch


def load_xor_data():
    x = torch.tensor([[0.0, 0.0],
                  [0.0, 1.0],
                  [1.0, 0.0],
                  [1.0, 1.0]])
    y = torch.tensor([0, 1, 1, 0])

    return [x, y]
