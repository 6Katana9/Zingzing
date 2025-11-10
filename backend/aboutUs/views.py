from rest_framework.views import APIView
from rest_framework.response import Response
from .models import HeroSection, SecondSection, ThirdSection

class AboutUsAPIView(APIView):
    def get(self, request):

        hero = HeroSection.objects.first()
        second = SecondSection.objects.first()
        third = ThirdSection.objects.first()

        return Response({
            "hero": {
                "title1": hero.title1,
                "mainTitleSpan1": hero.mainTitleSpan1,
                "title2": hero.title2,
                "mainTitleSpan2": hero.mainTitleSpan2,
                "text": hero.text,
                "leftSideImage1": hero.leftSideImage1.url,
                "leftSideImage2": hero.leftSideImage2.url,
                "leftSideImage3": hero.leftSideImage3.url,
                "rightSideImage": hero.rightSideImage.url,
            },
            "secondSection": {
                "mainTitle": second.mainTitle,
                "mainTitleSpan": second.mainTitleSpan,
                "list": [
                    {
                        "id": c.id,
                        "image": c.image.url,
                        "innerTitle": c.innerTitle,
                        "text": c.text
                    }
                    for c in second.list.all()
                ],
                "dropsList": [
                    {
                        "id": d.id,
                        "image": d.image.url,
                        "dropsTitle": d.dropsTitle,
                        "dropsText": d.dropsText,
                    }
                    for d in second.dropsList.all()
                ]
            },
            "thirdSection": {
                "blocks": [
                    {
                        "id": b.id,
                        "title": b.title,
                        "titleSpan": b.titleSpan,
                        "text": b.text,
                        "image": b.image.url
                    }
                    for b in third.blocks.all()
                ]
            }
        })
