<template>
	<div class="container is-fluid">
		<div class="tile is-ancestor">
			<div class="tile is-1" id="fix-tile">
				<div class="tile is-parent is-vertical">
						<StickyBar />
				</div>
			</div>
			<div class="tile">
				<div class="tile is-parent is-vertical" id="fix-parent">
					<div class="tile is-child color2">
						<HeaderRight />
					</div>
					<div class="tile is-child">
						<h1 class="title is-1">Sunat Exchange</h1>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	import StickyBar from './StickyBar.vue';
	import HeaderRight from './HeaderRight.vue';
	export default {
		name: 'Main',
		components: {
			StickyBar,
			HeaderRight,
		},
	};
</script>

<style lang="scss">
#fix-tile {
	position: absolute;
	left: -1%;
	right: 0;
}
.is-ancestor {
	width: 110%;
	text-align: right;
}
</style>
