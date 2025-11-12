from rest_framework.views import APIView
from rest_framework.response import Response
from .models import HeroSection, SecondSection, ThirdSection


class AboutUsAPIView(APIView):
    def get(self, request):
        hero = HeroSection.objects.first()
        second = SecondSection.objects.first()
        third = ThirdSection.objects.first()

        def absolute_url(file_field):
            if file_field:
                return request.build_absolute_uri(file_field.url)
            return None

        return Response({
            "hero": {
                "title1": hero.title1,
                "mainTitleSpan1": hero.mainTitleSpan1,
                "title2": hero.title2,
                "mainTitleSpan2": hero.mainTitleSpan2,
                "text": hero.text,
                "leftSideImage1": absolute_url(hero.leftSideImage1),
                "leftSideImage2": absolute_url(hero.leftSideImage2),
                "leftSideImage3": absolute_url(hero.leftSideImage3),
                "rightSideImage": absolute_url(hero.rightSideImage),
            },
            "secondSection": {
                "mainTitle": second.mainTitle,
                "mainTitleSpan": second.mainTitleSpan,
                "list": [
                    {
                        "id": c.id,
                        "image": absolute_url(c.image),
                        "innerTitle": c.innerTitle,
                        "text": c.text
                    }
                    for c in second.list.all()
                ],
                "dropsList": [
                    {
                        "id": d.id,
                        "image": absolute_url(d.image),
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
                        "image": absolute_url(b.image)
                    }
                    for b in third.blocks.all()
                ]
            }
        })
