<template>
	<div v-if="deviceType === 'desktop' ">
		<div class="columns is-desktop my-4 ml-6" id="fix-columns">
			<div class="column is-2 ml-6">
				<input class="input is-rounded custom-placeholder color3 text-color1" type="text" placeholder="Search...                󰍉">
			</div>
			<div class="column is-6">
				<h1 class="title is-3 has-text-centered text-color4">Dashboard</h1>
			</div>
			<div class="column">
				<div class="columns" id="fix-columns-icon">
					<div class="column">
						<span class="icon-text">
							<span class="icon">
								<i class="is-clickable" id="bell">  </i>
							</span>
						</span>
					</div>
					<div class="column">
						<div class="dropdown is-active is-right" :class="{'is-active': isDropdownActive}">
							<div class="dropdown-trigger">
								<span class="icon-text">
									<span class="icon">
										<i class="is-clickable" @click="toggleDropdown" id="user">  </i>
									</span>
								</span>
							</div>
							<div v-if="isDropdownActive" class="dropdown-menu" id="dropdown-menu" role="menu">
								<div class="dropdown-content">
									<a href="#" class="dropdown-item">
										Profile
									</a>
									<a href="#" class="dropdown-item">
										Logout
									</a>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	import { useDeviceType } from '@/composables/global.js'
	export default {
		name: 'Header',
		data() {
			return {
				isDropdownActive: false
			}
		},

		mounted() {
			document.addEventListener('click', this.handleClickOutside);
		},
		unmounted() {
			document.removeEventListener('click', this.handleClickOutside);
		},
		methods: {
			toggleDropdown() {
				this.isDropdownActive = !this.isDropdownActive;
			},
			handleClickOutside(e) {
				if (!this.$el.contains(e.target)) {
					this.isDropdownActive = false;
				}
			}
		},
		setup() {
			const { deviceType } = useDeviceType();
			return { deviceType };
		}
	}
</script>

<style lang="scss">
* {
	font-family: '3270NerdFont-Regular';
}
.custom-placeholder::placeholder {
	font-family: '3270NerdFont-Condensed';
	font-weight: bold;
	color: #12486B !important;
}
#bell {
	font-size: 1.4rem;
	color: #F5FCCD;
	font-style: normal !important;
}
#user {
	font-style: normal !important;
	font-size: 1.4rem;
	color: #F5FCCD;
}
.dropdown {
	z-index: 1000;
}
#fix-columns {
	width: 100%;
	padding: 0px 80px 0px 80px;
}
#fix-columns-icon {
	padding: 0px 0px 0px 180px;
	margin: 0px 80px 0px 80px;
}
</style>
