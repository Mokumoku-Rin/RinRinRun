from usecases.image import calc_image_similarity
from usecases.landmark import add_landmark, get_all_landmarks


class LandmarkService:
    @staticmethod
    async def ImageCompare(image_request):
        similarity = calc_image_similarity(
            image_request.img, image_request.landmark_id)
        threshold = 55
        print("DEBUG sim:", similarity)
        # similarityは、一致度が高いほど0に近くなるため
        if similarity < threshold:
            return "OK"
        return "NG"

    @staticmethod
    async def post_landmark(name, description, img_path, pos):
        add_landmark(name, description, img_path, pos)
        return 'OK'
    

    @staticmethod
    async def fetch_all_landmarks():
        landmark_list = get_all_landmarks()
        return landmark_list
