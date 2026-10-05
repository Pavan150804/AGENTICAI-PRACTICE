from huggingface_hub import scan_cache_dir

cache_info = scan_cache_dir()

print(cache_info.size_on_disk_str)
for repo in cache_info.repos:
    print(repo.repo_id)
    print(repo.size_on_disk_str)
    
import torch

print("CUDA available:", torch.cuda.is_available())
print("GPU count:", torch.cuda.device_count())