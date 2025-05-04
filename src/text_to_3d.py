import torch
from point_e.util.plotting import plot_point_cloud
from point_e.util.point_cloud import PointCloud
from point_e.models.download import load_checkpoint
from point_e.models.configs import MODEL_CONFIGS, model_from_config
import numpy as np

class TextTo3DGenerator:
    def __init__(self):
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        print(f"Using device: {self.device}")
        
        # Load the base model
        self.base_name = 'base40M'  # Changed from base40M-textvec
        self.base_model = model_from_config(MODEL_CONFIGS[self.base_name], self.device)
        self.base_model.eval()
        base_checkpoint = load_checkpoint(self.base_name, device=self.device)
        self.base_model.load_state_dict(base_checkpoint)

        # Load the text model
        self.text_name = 'base40M-textvec'
        self.text_model = model_from_config(MODEL_CONFIGS[self.text_name], self.device)
        self.text_model.eval()
        text_checkpoint = load_checkpoint(self.text_name, device=self.device)
        self.text_model.load_state_dict(text_checkpoint)

    def generate_point_cloud(self, text_prompt):
        """
        Generate point cloud from text description
        """
        try:
            # Generate embeddings from text
            text_embedding = self.text_model.get_text_embedding(text_prompt)
            
            # Sample points using the base model
            samples = None
            for x in self.base_model.sample(text_embedding):
                samples = x
            
            pc = PointCloud(samples.cpu().numpy())
            return pc
        except Exception as e:
            print(f"Error generating point cloud: {str(e)}")
            return None

    def save_to_obj(self, point_cloud, output_path):
        """
        Save point cloud to OBJ file
        """
        try:
            # Convert point cloud to mesh
            points = point_cloud.coords
            vertices = points.reshape(-1, 3)
            
            # Write to OBJ file
            with open(output_path, 'w') as f:
                for vertex in vertices:
                    f.write(f"v {vertex[0]} {vertex[1]} {vertex[2]}\n")
                
            print(f"Model saved to {output_path}")
            return True
        except Exception as e:
            print(f"Error saving to OBJ: {str(e)}")
            return False