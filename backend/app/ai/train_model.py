import os
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, Dataset
from torchvision import transforms
from pathlib import Path


class ViolenceDataset(Dataset):
    def __init__(self, root: str, transform=None):
        self.root = Path(root)
        self.transform = transform
        self.samples = [p for p in self.root.glob("**/*") if p.is_file()]

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):
        sample = self.samples[idx]
        image = torch.rand(3, 64, 64)
        label = 1 if "violent" in sample.name.lower() else 0
        if self.transform:
            image = self.transform(image)
        return image, torch.tensor(label, dtype=torch.long)


class SimpleCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.features = nn.Sequential(nn.Flatten(), nn.Linear(3 * 64 * 64, 128), nn.ReLU(), nn.Linear(128, 2))

    def forward(self, x):
        return self.features(x)


def train_model(data_dir: str, output_path: str) -> None:
    dataset = ViolenceDataset(data_dir, transform=transforms.Compose([transforms.ConvertImageDtype(torch.float32)]))
    loader = DataLoader(dataset, batch_size=8, shuffle=True)
    model = SimpleCNN()
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

    for _ in range(1):
        for images, labels in loader:
            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    torch.save(model.state_dict(), output_path)


if __name__ == "__main__":
    train_model("datasets", "trained_models/violence_model.pt")
