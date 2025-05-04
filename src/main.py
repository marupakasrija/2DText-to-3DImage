import os
from text_to_3d import TextTo3DGenerator

def main():
    # Create output directory if it doesn't exist
    output_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'output')
    os.makedirs(output_dir, exist_ok=True)

    # Initialize generator
    generator = TextTo3DGenerator()

    # Get user input
    text_prompt = input("Enter a description of the 3D object you want to generate: ")

    # Generate point cloud
    point_cloud = generator.generate_point_cloud(text_prompt)
    
    if point_cloud is not None:
        # Save to OBJ file
        output_path = os.path.join(output_dir, 'output_model.obj')
        generator.save_to_obj(point_cloud, output_path)

if __name__ == "__main__":
    main()