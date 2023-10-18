import imageio.v2 as imageio

filenames = ['team-pic1.png', 'team-pic2.png']
images = []

for filename in filenames:
    images.append(imageio.imread(filename))

imageio.mimsave('team.gif', images, duration=0.5)
