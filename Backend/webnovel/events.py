from models import SessionDep,NovelView,NovelRank,Novel
from fastapi_utils.tasks import repeat_every
from sqlmodel import Field, Session, SQLModel, create_engine, select

# @repeat_every(seconds=30) 
# async def demo():
#     print("hello task running") # 1 hour

#rank of novels...........
@repeat_every(seconds=15)
async def generate_rank_of_novels(session: SessionDep) -> dict:
    print("generating ranks event")
    novels = session.exec(select(NovelView).order_by(NovelView.total_views.desc())).all()
    print("msg: rank updated")
    print(novels)
    rank = 1
    for novel in novels:
        print(novel.novel_id)
        NovelRank(novel_id=novel.novel_id, rank=rank)  #todo :do i fetch latest novel rank instance s for a novel id or should i update old one
        rank += 1
    session.commit()

    return {'msg': "rank updated"} 
    