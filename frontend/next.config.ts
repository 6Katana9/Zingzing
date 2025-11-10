/** @type {import('next').NextConfig} */
const nextConfig = {
	images: {
		remotePatterns: [
			{
				protocol: 'http',
				hostname: '94.198.217.222',
				port: '',
				pathname: '/**',
			},
		],
	},
}

export default nextConfig
